using System.Net.Http.Json;

using MakrwatchClient.Contracts.V1;
using MakrwatchClient.Contracts.V1.Responses;
using MakrwatchClient.Infrastructure;
using MakrwatchClient.Models;
using MakrwatchClient.Services.Contracts;

namespace MakrwatchClient.Services
{
  public class SearchVideoService : ISearchVideoService
  {
    private readonly HttpClient _httpClient;

    public SearchVideoService(HttpClient httpClient)
    {
      _httpClient = httpClient;
    }

    public async Task<List<Video>> SearchYoutubeVideos(SearchFilter model)
    {
      var videos = new List<Video>();

      try
      {
        var url = string.Format(ApiRoutes.SearchVideos.Youtube, model.Keywords,
          model.MinSubscribers, model.MinViews, model.MaxViews, model.CountryCode);
        if (model.CountryCode.Equals(Constants.NullString))
        {
          url = string.Format(ApiRoutes.SearchVideos.YoutubeWithoutCountry, model.Keywords,
            model.MinSubscribers, model.MinViews, model.MaxViews);
        }

        var response = await _httpClient.GetFromJsonAsync<SearchVideoResponse>(url);

        if (response?.items != null)
        {
          foreach (var item in response.items)
          {
            videos.Add(
              new Video
              {
                Id = item.id,
                Title = item.title,
                Description = item.description,
                Url = item.url,
                ThumbnailUrl = item.thumbnail_url,
                PublishedAt = item.published_at,
                TotalViews = item.total_views,
                ChannelId = item.channel_id,
                ChannelTitle = item.channel_title,
                ChannelSubscribers = item.channel_subscribers,
                CountryCode = item.channel_country_code
              });
          }
        }
      }
      catch (Exception ex)
      {
        Console.WriteLine(ex);
      }

      return videos;
    }
  }
}
