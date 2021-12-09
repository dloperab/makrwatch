import pytest

from .steps.get_all_youtube_videos_steps import ShouldGetAllYoutubeVideosSteps
from src.domain.models.video import Video

YOUTUBE_VIDEOS__RETURN_DATA = [
    Video(id='th3uIP7D8nk', title='Spring Boot Restful Web Services Tutorial', description='In this course, you will learn how to build REST APIs using Spring boot', url='https://www.youtube.com/watch?v=th3uIP7D8nk', thumbnail_url='https://i.ytimg.com/vi/th3uIP7D8nk/hqdefault.jpg', published_at='2021-06-30T14:07:18Z', total_views=36552, channel_id='UC1Be9fnFTlcsUlejgfqag0g', channel_title='Java Guides', channel_subscribers=51700, channel_country_code='IN'),
    Video(id='cm9cCymt1y0', title='Part 7- Rest API Microservices| How To Create Rest API Microservice using SpringBoot |JPA| MySQL', description='#RestAPI#Microservices#SpringBoot#jp', url='https://www.youtube.com/embed/cm9cCymt1y0?autoplay=0', thumbnail_url='https://i.ytimg.com/vi/cm9cCymt1y0/hqdefault.jpg', published_at='2021-06-25T14:30:12Z', total_views=8074, channel_id='UC46vj6mN-6kZm5RYWWqebsg', channel_title='SDET- QA Automation Techie', channel_subscribers=238000, channel_country_code='IN')
]

KEYWORDS = 'develop rest services'
COUNTRY_CODE = 'US'
COUNTRY_CODE_NONE = None
MIN_SUBSCRIBERS = 1500
MIN_VIDEO_VIEWS = 2500
MAX_VIDEO_VIEWS = 30000

@pytest.mark.parametrize(
    "keywords, country_code, min_subscribers, min_video_views, max_video_views, youtube_videos", 
    [(KEYWORDS, COUNTRY_CODE, MIN_SUBSCRIBERS, MIN_VIDEO_VIEWS, MAX_VIDEO_VIEWS, YOUTUBE_VIDEOS__RETURN_DATA)]
)
def test_should_get_all_youtube_videos_all_params(keywords, country_code, min_subscribers, min_video_views, 
    max_video_views, youtube_videos):
    steps = ShouldGetAllYoutubeVideosSteps()
    steps.given(keywords, country_code, min_subscribers, min_video_views, max_video_views, youtube_videos)
    steps.when()
    steps.then()

@pytest.mark.parametrize(
    "keywords, country_code, min_subscribers, min_video_views, max_video_views, youtube_videos", 
    [(KEYWORDS, COUNTRY_CODE_NONE, MIN_SUBSCRIBERS, MIN_VIDEO_VIEWS, MAX_VIDEO_VIEWS, YOUTUBE_VIDEOS__RETURN_DATA)]
)
def test_should_get_all_youtube_videos_country_param_none(keywords, country_code, min_subscribers, min_video_views, 
    max_video_views, youtube_videos):
    steps = ShouldGetAllYoutubeVideosSteps()
    steps.given(keywords, country_code, min_subscribers, min_video_views, max_video_views, youtube_videos)
    steps.when()
    steps.then()
