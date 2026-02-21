from database import supabase
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def chat_with_rag(question):

    query_embedding = client.embeddings.create(
        model="text-embedding-3-small",
        input=question
    ).data[0].embedding

    response = supabase.rpc("match_chunks", {
        "query_embedding": query_embedding,
        "match_count": 5
    }).execute()

    context = "\n".join([item["content"] for item in response.data])

    prompt = f"""
    Answer ONLY using this context:

    {context}

    Question: {question}
    """

    answer = client.responses.create(
        model="gpt-4.1",
        input=prompt
    )

    return {"answer": answer.output[0].content[0].text}