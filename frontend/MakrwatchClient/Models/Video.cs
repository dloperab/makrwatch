using MakrwatchClient.Helpers;
using MakrwatchClient.Infrastructure;

namespace MakrwatchClient.Models
{
  public class Video
  {
    public string Id { get; set; }
    public string Title { get; set; }
    public string Description { get; set; }
    public string Url { get; set; }
    public string ThumbnailUrl { get; set; }
    public string PublishedAt { get; set; }
    public int TotalViews { get; set; }
    public string ChannelId { get; set; }
    public string ChannelTitle { get; set; }
    public int ChannelSubscribers { get; set; }
    public string CountryCode { get; set; }

    public string DescriptionWrapped
    {
      get
      {
        var shortDescription = Description;

        if (Description is not null && Description.Length > SearchConstants.MaxTextCharacters)
        {
          shortDescription = Description.Substring(0, SearchConstants.MaxTextCharacters);
          shortDescription += Constants.Ellipsis;
        }

        return shortDescription;
      }
    }

    public string Stats => string.Format(SearchResources.VideoStatsText, 
      NumberHelpers.GetShortText(TotalViews), 
      NumberHelpers.GetShortText(ChannelSubscribers));    

    public Video() { }

    public Video(string id, string title, string description, string url, string thumbnailUrl, string publishedAt, 
      int totalViews, string channelId, string channelTitle, int channelSubscribers, string countryCode)
    {
      Id = id;
      Title = title;
      Description = description;
      Url = url;
      ThumbnailUrl = thumbnailUrl;
      PublishedAt = publishedAt;
      TotalViews = totalViews;
      ChannelId = channelId;
      ChannelTitle = channelTitle;
      ChannelSubscribers = channelSubscribers;
      CountryCode = countryCode;
    }
  }
}
