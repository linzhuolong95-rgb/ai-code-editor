from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="AI Code Editor API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MOOTA_API_TOKEN = os.getenv("MOOTA_API_TOKEN")

@app.get("/")
async def root():
    return {"message": "Welcome to AI Code Editor API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}