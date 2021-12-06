from dotenv import load_dotenv
from fastapi import FastAPI

from . import videos_endpoint

load_dotenv()

def create_app():
    app = FastAPI(title="Makrwatch API", version="v1")
    app.include_router(videos_endpoint.router)

    return app
