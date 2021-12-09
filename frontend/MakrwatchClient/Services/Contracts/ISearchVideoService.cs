using MakrwatchClient.Models;

namespace MakrwatchClient.Services.Contracts
{
  public interface ISearchVideoService
  {
    Task<List<Video>> SearchYoutubeVideos(SearchFilter model);
  }
}
