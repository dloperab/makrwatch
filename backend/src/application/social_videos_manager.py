from typing import List

from domain.models import Video
from domain.repositories import YoutubeRepositoryInterface

class SocialVideosManager():
    """
    Class to manage the social videos networks
    """

    def __init__(self, youtube_repository: YoutubeRepositoryInterface):
        self.youtube_repository = youtube_repository

    def search_youtube_videos(self, keywords: str, country_code: None, min_subscribers: int, 
        min_video_views: int, max_video_views: int) -> List[Video]:
        """Method to search videos on Youtube.

        Args:
            keywords (str): The keywords to search.
            country_code (None): The country code to search.
            min_subscribers (int): The minimum number of subscribers to search.
            min_video_views (int): The minimum number of views to search.
            max_video_views (int): The maximum number of views to search.

        Returns:
            List[Video]: Videos found on Youtube
        """

        return self.youtube_repository.search(keywords, country_code, min_subscribers, 
            min_video_views, max_video_views)
