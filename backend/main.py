"""DigiDex Backend - FastAPI BFF for Digi-API."""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.v1.digimon import router as digimon_router
from services.digi_api import digi_api_client


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage app lifecycle - cleanup HTTP client on shutdown."""
    yield
    await digi_api_client.close()


app = FastAPI(
    title="DigiDex API",
    description="Backend-for-Frontend layer for the Digital Gate application",
    version="1.0.0",
    lifespan=lifespan,
)

# CORS configuration - allow frontend origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # SvelteKit dev
        "http://localhost:4173",  # SvelteKit preview
        "http://127.0.0.1:5173",
        "http://127.0.0.1:4173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount API routes
app.include_router(digimon_router, prefix="/api/v1")


@app.get("/")
async def root():
    """Health check endpoint."""
    return {"status": "online", "service": "DigiDex API", "version": "1.0.0"}


@app.get("/health")
async def health():
    """Health check for deployment platforms."""
    return {"status": "healthy"}
