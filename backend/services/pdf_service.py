from pypdf import PdfReader
from utils import chunk_text
from database import supabase
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def process_pdf(file):
    reader = PdfReader(file.file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

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

    return {"message": "PDF processed successfully"}