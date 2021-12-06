import os

from fastapi import Depends
from googleapiclient.discovery import build

from domain.repositories import YoutubeRepositoryInterface
from data import YoutubeApiRepository
from application import SocialVideosManager

def youtube_service_module():
    api_key = "os.environ.get(YOUTUBE_API_KEY)"
    return build("youtube", "v3", api_key)

def youtube_api_repository_module(
    youtube_service = Depends(youtube_service_module),
) -> YoutubeRepositoryInterface: 
    return YoutubeApiRepository(youtube_service)

def social_videos_manager_module(
    youtube_api_repository: YoutubeApiRepository = Depends(
        youtube_api_repository_module
    ),
) -> SocialVideosManager:
    return SocialVideosManager(youtube_api_repository)
