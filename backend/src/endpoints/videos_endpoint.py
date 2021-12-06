from fastapi import APIRouter
from fastapi import Depends

from di import providers

router = APIRouter()

@router.get("/api/v1/videos/youtube")
def search_youtube_videos(social_videos_manager=Depends(providers.social_videos_manager_module)):
    try:
        videos_response = social_videos_manager.search_youtube_videos("developi rest services", country_code='IS', 
            min_subscribers=1000, min_video_views=1500, max_video_views=2500)
        
        return {"items": videos_response}
    except Exception as e:
        return {"error": str(e)}
