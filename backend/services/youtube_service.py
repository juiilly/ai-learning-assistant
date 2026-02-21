from youtube_transcript_api import YouTubeTranscriptApi
from utils import chunk_text
from database import supabase
from openai import OpenAI
import os
import re

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


async def process_youtube(url: str):
    try:
        # 1️⃣ Extract Video ID
        video_id = extract_video_id(url)

        # 2️⃣ Fetch transcript (latest working method)
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id)

        # 3️⃣ Combine transcript into one text
        text = " ".join([t["text"] for t in transcript_data])

        if not text.strip():
            return {"error": "Transcript is empty"}

        # 4️⃣ Chunk text
        chunks = chunk_text(text)

        # 5️⃣ Generate embeddings + store in Supabase
        for chunk in chunks:
            embedding_response = client.embeddings.create(
                model="text-embedding-3-small",
                input=chunk
            )

            embedding = embedding_response.data[0].embedding

            supabase.table("chunks").insert({
                "content": chunk,
                "embedding": embedding
            }).execute()

        return {"message": "Video processed successfully"}

    except Exception as e:
        return {"error": str(e)}


def extract_video_id(url: str):
    """
    Extracts YouTube video ID from multiple URL formats
    """
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11})"
    match = re.search(pattern, url)

    if not match:
        raise ValueError("Invalid YouTube URL")

    return match.group(1)