using Microsoft.AspNetCore.Components;
using Microsoft.AspNetCore.Components.Forms;

using MakrwatchClient.Models;
using MakrwatchClient.Infrastructure;
using MakrwatchClient.Services.Contracts;

namespace MakrwatchClient.Pages
{
  public partial class Index : ComponentBase
  {
    [Inject]
    public ILocationService LocationService { get; set; }

    [Inject]
    public ISearchVideoService SearchVideoService { get; set; }

    private bool IsWaiting { get; set; } = false;

    private IEnumerable<int> _totalViewsValues = new int[] { SearchConstants.RangeMinViews, SearchConstants.RangeMaxViews };
    private EditContext _editContext;

    private string _searchResults = string.Empty;
    private readonly SearchFilter _model = new();
    private List<Location> _locations = new();
    private List<Video> _videos = new();

    protected override void OnInitialized()
    {
      try
      {
        IsWaiting = true;

        _locations = LocationService.GetLocations();

        _searchResults = SearchResources.SearchResultsTextEmpty;
        _editContext = new EditContext(_model);
      }
      catch (Exception ex)
      {
        Console.WriteLine($"[ERROR] {ex}");
      }
      finally
      {
        IsWaiting = false;
      }
    }

    void OnTotalViewsChange(dynamic value)
    {
      var views = string.Join(Constants.CommaSeparator, value).Split(Constants.CommaSeparator);
      _model.ConvertNewViews(Convert.ToInt32(views[0]), Convert.ToInt32(views[1]));
    }

    private async Task HandleOnSearchSubmit()
    {
      try
      {
        IsWaiting = true;

        _videos.Clear();
        _videos = await SearchVideoService.SearchYoutubeVideos(_model);
        _searchResults = string.Format(SearchResources.SearchResultsText, _videos.Count);
      }
      catch (Exception ex)
      {
        Console.WriteLine($"[ERROR] {ex}");
      }
      finally
      {
        IsWaiting = false;
      }
    }
  }
}
