# ai-learning-assistant


📌 Overview

AI-powered Learning Assistant that allows users to:

Process YouTube transcripts

Upload and process PDFs

Generate Flashcards

Generate Quizzes (MCQs)

Chat with content using RAG (Retrieval-Augmented Generation)

🏗 Tech Stack

Frontend

Next.js (App Router)

TailwindCSS

Backend

FastAPI (Python)

Database

Supabase (Postgres + pgvector)

AI Models

OpenAI GPT-4.1

text-embedding-3-small

🚀 Features

1️⃣ YouTube Processing

Extracts transcript using youtube-transcript-api

Chunks content

Generates embeddings

Stores in Supabase vector database

2️⃣ PDF Processing

Extracts text using PyPDF2

Chunks content

Stores embeddings in vector DB

3️⃣ Flashcards Generation

Generates 10–15 flashcards

Structured JSON format

4️⃣ Quiz Generation

Generates 5–10 MCQs

Includes correct answer

Auto-evaluation supported

5️⃣ RAG Chat System

Vector similarity search using pgvector

Context-aware responses

Embedding-based retrieval

🔌 API Endpoints
Endpoint	Method	Description
/process-video	POST	Process YouTube transcript
/process-pdf	POST	Process uploaded PDF
/generate-flashcards	POST	Generate flashcards
/generate-quiz	POST	Generate MCQs
/chat	POST	RAG-based contextual chat

🧠 Architecture Overview

Content is extracted (YouTube/PDF)

Text is chunked

Embeddings generated using OpenAI

Stored in Supabase pgvector

User queries perform similarity search

Retrieved context sent to GPT-4.1

AI generates response

⚙️ Setup Instructions
1️⃣ Clone Repository
git clone <your-repo-url>
cd backend
2️⃣ Install Dependencies
pip install -r requirements.txt

Or manually:

pip install fastapi uvicorn openai supabase youtube-transcript-api PyPDF2 python-dotenv
3️⃣ Configure Environment Variables

Create .env file:

OPENAI_API_KEY=your_openai_key
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
4️⃣ Run Backend
uvicorn main:app --reload

Access Swagger:

http://127.0.0.1:8000/docs
🗄 Supabase Setup

Run this SQL in Supabase SQL Editor:

create extension if not exists vector;

create table documents (
  id uuid primary key default uuid_generate_v4(),
  content text,
  embedding vector(1536)
);

Add similarity RPC function for vector search.



👩‍💻 Developed By

Juily Bagate
BTech – Computer Science Engineering
