URL_WITHOUT_COUNTRY_CODE = '/api/v1/videos/youtube?keywords=develop%20rest%20services&min_subscribers=1500&min_video_views=2500&max_video_views=30000'
URL_WITH_COUNTRY_CODE = '/api/v1/videos/youtube?keywords=develop%20rest%20services&min_subscribers=1500&min_video_views=2500&max_video_views=30000&country_code=US'
URL_WITHOUT_VALS = '/api/v1/videos/youtube'

def test_get_all_videos_without_country_code(client):
    response = client.get(URL_WITHOUT_COUNTRY_CODE)
    assert response.status_code == 200

def test_get_all_videos_with_country_code(client):
    response = client.get(URL_WITH_COUNTRY_CODE)
    assert response.status_code == 200

def test_get_all_videos_without_vals(client):
    response = client.get(URL_WITHOUT_VALS)
    assert response.status_code == 422
