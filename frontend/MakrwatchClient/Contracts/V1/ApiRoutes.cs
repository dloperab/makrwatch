namespace MakrwatchClient.Contracts.V1
{
  public static class ApiRoutes
  {
    public const string Root = "http://localhost:8080/";
    public const string Version = "v1";
    public const string Base = "/api/" + Version;

    public static class SearchVideos
    {
      public const string Youtube = Base + "/videos/youtube?keywords={0}&min_subscribers={1}&min_video_views={2}&max_video_views={3}&country_code={4}";
      public const string YoutubeWithoutCountry = Base + "/videos/youtube?keywords={0}&min_subscribers={1}&min_video_views={2}&max_video_views={3}";
    }
  }
}
