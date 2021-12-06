from abc import (
    ABCMeta,
    abstractmethod
)

from typing import List

from ..models import Video

class YoutubeRepositoryInterface:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def search_videos(self, keywords: str, country_code: None, min_subscribers: int, 
        min_video_views: int, max_video_views: int) -> List[Video]:
        pass  # pragma: no coverColo
