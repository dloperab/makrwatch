
namespace MakrwatchClient.Contracts.V1.Responses
{
  public class Item
  {
    public string id { get; set; }
    public string title { get; set; }
    public string description { get; set; }
    public string url { get; set; }
    public string thumbnail_url { get; set; }
    public string published_at { get; set; }
    public int total_views { get; set; }
    public string channel_id { get; set; }
    public string channel_title { get; set; }
    public int channel_subscribers { get; set; }
    public string channel_country_code { get; set; }
  }

  public class SearchVideoResponse
  {
    public List<Item> items { get; set; }
  }
}
