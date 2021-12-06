from typing import List

from domain.models import Video
from domain.repositories import YoutubeRepositoryInterface

class SocialVideosManager():
    def __init__(self, youtube_repository: YoutubeRepositoryInterface):
        self.youtube_repository = youtube_repository

    def search_youtube_videos(self, keywords: str, country_code: None, min_subscribers: int, 
        min_video_views: int, max_video_views: int) -> List[Video]:

        return self.youtube_repository.search(keywords, country_code, min_subscribers, 
            min_video_views, max_video_views)
