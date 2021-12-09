from dataclasses import dataclass

@dataclass
class Video:
    '''
    Video class to manage video data
    '''

    id: str
    title: str
    description: str
    url: str
    thumbnail_url: str
    published_at: str
    total_views: int
    channel_id: str
    channel_title: str
    channel_subscribers: int
    channel_country_code: str
