import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.v1.digimon import router as digimon_router
from services.digi_api import digi_api_client

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await digi_api_client.close()

app = FastAPI(
    title="DigiDex API",
    description="Backend-for-Frontend layer for the Digital Gate application",
    version="1.0.0",
    lifespan=lifespan,
)

# CORS - Allow frontend origins
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")
allowed_origins = [
    "http://localhost:5173",
    "http://localhost:4173",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:4173",
    "https://diegorodriguez3d.github.io",
]

# Add production frontend URL if configured
if FRONTEND_URL and FRONTEND_URL not in allowed_origins:
    allowed_origins.append(FRONTEND_URL)

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(digimon_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"status": "online", "service": "DigiDex API", "version": "1.0.0"}


@app.get("/health")
async def health():
    return {"status": "healthy"}
