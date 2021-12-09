from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv

from . import videos_endpoint

origins = ["*"]

# Load environment variables from .env file
load_dotenv()

def create_app():
    """
    Create the FastAPI application.
    """

    app = FastAPI(title="Makrwatch API", version="v1")
    app.include_router(videos_endpoint.router)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
