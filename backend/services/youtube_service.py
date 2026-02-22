import os
import re
from openai import OpenAI
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
from utils import chunk_text
from database import supabase

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def extract_video_id(url: str):
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11})"
    match = re.search(pattern, url)
    if not match:
        raise ValueError("Invalid YouTube URL")
    return match.group(1)


async def process_youtube(url: str):
    try:
        video_id = extract_video_id(url)

        try:
            transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
        except TranscriptsDisabled:
            return {"error": "Subtitles are disabled for this video"}
        except NoTranscriptFound:
            return {"error": "No transcript found for this video"}

        text = " ".join([t["text"] for t in transcript_data])

        if not text.strip():
            return {"error": "Transcript is empty"}

        chunks = chunk_text(text)

        for chunk in chunks:
            embedding = client.embeddings.create(
                model="text-embedding-3-small",
                input=chunk
            ).data[0].embedding

            supabase.table("chunks").insert({
                "content": chunk,
                "embedding": embedding
            }).execute()

        return {"message": "Video processed successfully"}

    except Exception as e:
        return {"error": str(e)}