import os
from typing_extensions import Final

from fastapi import Depends

from googleapiclient.discovery import build

from domain.repositories import YoutubeRepositoryInterface
from data import YoutubeApiRepository
from application import SocialVideosManager

YOUTUBE_API_KEY: Final = "YOUTUBE_API_KEY"

def youtube_service_module():
    '''
    Builds a Youtube Service instance based on Youtube API client library.
    '''

    api_key = os.environ.get(YOUTUBE_API_KEY)
    return build('youtube', 'v3', developerKey=api_key)

def youtube_api_repository_module(
    youtube_service = Depends(youtube_service_module),
) -> YoutubeRepositoryInterface:
    '''
    Builds a YoutubeApiRepository instance implementing YoutubeRepositoryInterface.
    '''

    return YoutubeApiRepository(youtube_service)

def social_videos_manager_module(
    youtube_api_repository: YoutubeApiRepository = Depends(
        youtube_api_repository_module
    ),
) -> SocialVideosManager:
    '''
    Builds a SocialVideosManager passing YoutubeApiRepository.
    '''

    return SocialVideosManager(youtube_api_repository)
