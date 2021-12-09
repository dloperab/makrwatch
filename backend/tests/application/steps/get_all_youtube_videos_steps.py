from unittest.mock import Mock

from src.application import SocialVideosManager

class ShouldGetAllYoutubeVideosSteps:
    def given(self, keywords, country_code, min_subscribers, 
        min_video_views, max_video_views, youtube_videos_mock):
        self.keywords = keywords
        self.country_code = country_code
        self.min_subscribers = min_subscribers
        self.min_video_views = min_video_views
        self.max_video_views = max_video_views
        self.youtube_videos_mock = youtube_videos_mock
        self.youtube_repository = Mock()
        self.youtube_repository.search = Mock(
            return_value=youtube_videos_mock
        )
        self.social_video_manager = SocialVideosManager(
            self.youtube_repository
        )

    def when(self):
        self.response = self.social_video_manager.search_youtube_videos(
            self.keywords, self.country_code, self.min_subscribers, 
            self.min_video_views, self.max_video_views
        )

    def then(self):
        assert self.response is not None
        assert len(self.response) == len(self.youtube_videos_mock)

        for youtube_videos, youtube_videos_mock in zip(self.response, self.youtube_videos_mock):
            assert youtube_videos.id == youtube_videos_mock.id
            assert youtube_videos.title == youtube_videos_mock.title
            assert youtube_videos.description == youtube_videos_mock.description
            assert youtube_videos.url == youtube_videos_mock.url
            assert youtube_videos.thumbnail_url == youtube_videos_mock.thumbnail_url
            assert youtube_videos.published_at == youtube_videos_mock.published_at
            assert youtube_videos.total_views == youtube_videos_mock.total_views
            assert youtube_videos.channel_id == youtube_videos_mock.channel_id
            assert youtube_videos.channel_title == youtube_videos_mock.channel_title
            assert youtube_videos.channel_country_code == youtube_videos_mock.channel_country_code
            assert youtube_videos.channel_subscribers == youtube_videos_mock.channel_subscribers

        self.youtube_repository.search.assert_called()
