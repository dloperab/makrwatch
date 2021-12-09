namespace MakrwatchClient.Infrastructure
{
  public class SearchConstants
  {
    protected SearchConstants() { }

    public const int MinSubscribersFilter = 10000;
    public const int MinViewsFilter = 10000;
    public const int MaxViewsFilter = 100000000;
    public const int ViewsMultiplier = 1000;
    public const int RangeMinViews = 10;
    public const int RangeMaxViews = 1000;
    public const int Subscribers10K = 10000;
    public const int Subscribers60K = 60000;
    public const int Subscribers300K = 300000;
    public const int Subscribers1M = 1000000;
    public const int MaxTextCharacters = 500;
  }
}
