from typing import List

from domain.models import Video
from domain.repositories import YoutubeRepositoryInterface

class YoutubeApiRepository(YoutubeRepositoryInterface):
    def __init__(self, youtube_service):
        self._max_results = 20
        self._channels_cache = dict()
        self._yt_service = youtube_service

    def search(self, keywords: str, country_code: None, min_subscribers: int, 
        min_video_views: int, max_video_views: int) -> List[Video]:
        videos_result: List[Video] = []

        search_nextToken = None
        while True:
            videos_response = self._search_videos(keywords, country_code, search_nextToken)
            search_nextToken = videos_response['nextPageToken']

            for video_response in videos_response['items']:
                # get channel stats
                channel_stats = self._get_channel_stats(video_response['snippet']['channelId'])
                channel_subscribers = channel_stats['items'][0]['statistics']['subscriberCount']
                if channel_subscribers <= min_subscribers:
                    continue

                # get video stats
                video_stats = self._get_video_stats(video_response['id']['videoId'])
                video_views = video_stats['items'][0]['statistics']['viewCount']
                #if min_video_views <= video_views <= max_video_views:
                if video_views >= min_video_views:
                    if len(videos_result) <= self._max_results:
                        video = Video(
                            id=video_response['id']['videoId'],
                            title=video_response['snippet']['title'],
                            description=video_stats['items'][0]['snippet']['description'],
                            url=f"https://www.youtube.com/watch?v={video_response['id']['videoId']}",
                            thumbnail_url=video_response['snippet']['thumbnails']['high']['url'],
                            published_at=video_response['snippet']['publishedAt'],
                            total_views=video_views,
                            channel_id=video_response['snippet']['channelId'],
                            channel_title=video_response['snippet']['channelTitle'],
                            channel_subscribers=channel_subscribers,
                            channel_country_code=channel_stats['items'][0]['snippet']['country']
                        )

                        videos_result.append(video)

                if len(videos_result) >= self._max_results:
                    break

            if len(videos_result) >= self._max_results:
                break

        return videos_result

    def _search_videos(self, search_string, country_code, token=None):
        request = self._yt_service.search().list(
            part='id,snippet',
            type='video',
            q=search_string,
            order='date',
            maxResults=self._max_results * 2,
            regionCode=country_code,
            pageToken=token,
            fields='nextPageToken,items(id(videoId),snippet(channelId,channelTitle,publishedAt,thumbnails/high/url,title))'
        )
        
        return request.execute()

    def _search_channel(self, channel_id):
        request = self._yt_service.channels().list(
            part='snippet,contentDetails,statistics',
            id=channel_id,
            fields='items(id,snippet(country),statistics(subscriberCount))'
        )

        return request.execute()

    def _search_video(self, video_id):
        request = self._yt_service.videos().list(
            part='snippet,statistics',
            id=video_id,
            fields='items(id,snippet(description),statistics(viewCount))'
        )

        return request.execute()

    def _get_channel_stats(self, channel_id):
        channel_stats = None  
        if channel_id in self._channels_cache:
            channel_stats = self._channels_cache[channel_id]
        else:
            channel_stats = self._search_channel(channel_id)
            if 'subscriberCount' in channel_stats['items'][0]['statistics']:
                channel_stats['items'][0]['statistics']['subscriberCount'] = int(channel_stats['items'][0]['statistics']['subscriberCount'])
            else:
                channel_stats['items'][0]['statistics']['subscriberCount'] = 0

            if 'country' not in channel_stats['items'][0]['snippet']:
                channel_stats['items'][0]['snippet']['country'] = 'US'

            self._channels_cache[channel_id] = channel_stats

        return channel_stats

    def _get_video_stats(self, video_id):
        video_stats = self._search_video(video_id)
        video_stats['items'][0]['statistics']['viewCount'] = int(video_stats['items'][0]['statistics']['viewCount'])
        
        return video_stats
