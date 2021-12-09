from typing import List
from typing_extensions import Final

from domain.models import Video
from domain.repositories import YoutubeRepositoryInterface

MAX_RESULTS: Final = 100

class YoutubeApiRepository(YoutubeRepositoryInterface):
    def __init__(self, youtube_service):
        self._yt_service = youtube_service
        self._videos_response = []
        self._videos_stats = {}
        self._channels_stats = {}

    def search(self, keywords: str, country_code: None, min_subscribers: int, 
        min_video_views: int, max_video_views: int) -> List[Video]:
        videos_result: List[Video] = []
        
        # search videos
        videos_response = self._search_videos(keywords, country_code)
        if not videos_response:
            return videos_result

        # get unique channels and search for channels stats filtering the min subscribers
        unique_channels = self._get_unique_channel_ids()
        self._get_channels_stats_filtered(unique_channels, min_subscribers)

        # get videos ids for channels and search for videos stats filtering the min and max views
        videos_ids = self._get_videos_ids_for_channels()
        self._get_videos_stats_filtered(videos_ids, min_video_views, max_video_views)

        # create videos response
        for video_id in self._videos_stats:
            videos_result.append(self._get_video_info(video_id))

        return videos_result

    def _search_videos(self, search_string, country_code, token=None):
        videos_result = []
        
        request = self._yt_service.search().list(
            part='id,snippet',
            type='video',
            q=search_string,
            order='date',
            maxResults=MAX_RESULTS,
            regionCode=country_code,
            pageToken=token,
            fields='nextPageToken,items(id(videoId),snippet(channelId,channelTitle,publishedAt,thumbnails/high/url,title))'
        )        
        videos_result = request.execute()

        if 'items' in videos_result:
            videos_result = videos_result['items']

        self._videos_response = videos_result

        return videos_result

    def _get_unique_channel_ids(self):
        unique_channels = list(set([item['snippet']['channelId'] for item in self._videos_response]))

        return unique_channels

    def _get_channels_stats_filtered(self, channels_id, min_suscribers):
        channels_stats = {}
        channels_response = []

        # search channels stats
        request = self._yt_service.channels().list(
            part='snippet,contentDetails,statistics',
            id=channels_id,
            fields='items(id,snippet(country),statistics(subscriberCount))'
        )
        response = request.execute()
        
        if 'items' in response:
            channels_response = response['items']

        # iterate every channel, convert data types and evaluate filter to select 
        # only the channels that apply to the search        
        for item in channels_response:
            if 'subscriberCount' in item['statistics']:      
                item['statistics']['subscriberCount'] = int(item['statistics']['subscriberCount'])
            else:
                item['statistics']['subscriberCount'] = 0

            if 'country' not in item['snippet']:
                item['snippet']['country'] = 'US'

            # validate channel
            if item['statistics']['subscriberCount'] >= min_suscribers:
                channels_stats[item['id']] = item

        self._channels_stats = channels_stats

        return channels_stats

    def _get_videos_ids_for_channels(self):
        videos_ids = [item['id']['videoId'] for item in self._videos_response if item['snippet']['channelId'] in self._channels_stats]

        return videos_ids

    def _get_videos_stats_filtered(self, videos_id, min_video_views, max_video_views):
        videos_stats = {}
        videos_reponse = []

        request = self._yt_service.videos().list(
            part='snippet,statistics',
            id=videos_id,
            fields='items(id,snippet(description),statistics(viewCount))'
        )
        response = request.execute()

        if 'items' in response:
            videos_reponse = response['items']

        # iterate every videos, convert data types and evaluate filter to select 
        # only the videos that apply to the search
        for item in videos_reponse:
            item['statistics']['viewCount'] = int(item['statistics']['viewCount'])  

            # validate channel
            if min_video_views <= item['statistics']['viewCount'] <= max_video_views:
            # if item['statistics']['viewCount'] >= min_video_views:
                videos_stats[item['id']] = item

        self._videos_stats = videos_stats

        return videos_stats

    def _get_video_info(self, video_id) -> Video:
        video_info = [video for video in self._videos_response if video['id']['videoId'] == video_id][0]

        channel_id = video_info['snippet']['channelId']
        video_stats = self._videos_stats[video_id]
        channel_stats = self._channels_stats[channel_id]

        video = Video(
            id = video_id,
            title = video_info['snippet']['title'],
            description = video_stats['snippet']['description'],
            url = f"https://www.youtube.com/embed/{video_id}?autoplay=0",
            thumbnail_url = video_info['snippet']['thumbnails']['high']['url'],
            published_at = video_info['snippet']['publishedAt'],
            total_views = video_stats['statistics']['viewCount'],
            channel_id = channel_id,
            channel_title = video_info['snippet']['channelTitle'],
            channel_subscribers = channel_stats['statistics']['subscriberCount'],
            channel_country_code = channel_stats['snippet']['country']
        )

        return video
