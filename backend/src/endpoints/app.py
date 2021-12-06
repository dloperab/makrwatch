# from dotenv import load_dotenv
from fastapi import FastAPI

from . import videos_endpoint

def create_app():
    app = FastAPI(title="Makrwatch API", description="Makrwatch API to search for videos on YouTube and other social networks", version="v1")
    app.include_router(videos_endpoint.router)

    return app
