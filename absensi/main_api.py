from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.ini_api import absensi_api

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://localhost:3001",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def Start():
    return {
        "status": 200,
        "message": "OK",
    }
    
app.include_router(absensi_api.router, tags=['Absensi'], prefix='/absensi/v1')