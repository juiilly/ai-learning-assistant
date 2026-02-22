from fastapi import FastAPI, UploadFile, File, Query
from fastapi.middleware.cors import CORSMiddleware
from services.youtube_service import process_youtube
from services.pdf_service import process_pdf
from rag import chat_with_rag
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

origins = [
    "https://shiny-space-dollop-977765xrj4q4f779q-3000.app.github.dev/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Root route (prevents 404 on base URL)
@app.get("/")
async def root():
    return {"message": "Backend is running 🚀"}

# ✅ Process YouTube Video
@app.post("/process-video")
async def process_video(url: str = Query(...)):
    try:
        return await process_youtube(url)
    except Exception as e:
        return {
            "error": str(e)
        }

# ✅ Process PDF Upload
@app.post("/process-pdf")
async def process_pdf_route(file: UploadFile = File(...)):
    return await process_pdf(file)

# ✅ Chat Endpoint
@app.post("/chat")
async def chat(question: str = Query(...)):
    return await chat_with_rag(question)