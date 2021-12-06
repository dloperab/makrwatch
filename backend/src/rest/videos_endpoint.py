from typing import Optional
from fastapi import APIRouter
from fastapi import Depends

from di import providers

router = APIRouter()

@router.get("/api/v1/videos/youtube")
def search_youtube_videos(
    keywords: str,    
    min_subscribers: int,
    min_video_views: int,
    max_video_views: int,
    country_code: Optional[str] = None,
    social_videos_manager=Depends(providers.social_videos_manager_module)):
    try:
        videos_response = social_videos_manager.search_youtube_videos(keywords, country_code, 
            min_subscribers, min_video_views, max_video_views)
        
        return {"items": videos_response}
    except Exception as e:
        return {"error": str(e)}
