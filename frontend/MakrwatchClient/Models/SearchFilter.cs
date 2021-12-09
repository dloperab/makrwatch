using System.ComponentModel.DataAnnotations;

using MakrwatchClient.Helpers;
using MakrwatchClient.Infrastructure;

namespace MakrwatchClient.Models
{
  public class SearchFilter
  {
    [Required]
    [Display(Name = "Keywords")]
    public string Keywords { get; set; } = string.Empty;

    public string CountryCode { get; set; } = Constants.NullString;

    [Required]
    public int MinSubscribers = SearchConstants.MinSubscribersFilter;

    [Required]
    public int MinViews = SearchConstants.MinViewsFilter;

    [Required]
    public int MaxViews = SearchConstants.MaxViewsFilter;

    public string MinViewsText => NumberHelpers.GetShortText(MinViews);

    public string MaxViewsText => NumberHelpers.GetShortText(MaxViews);

    public void ConvertNewViews(int newMinViews, int newMaxViews)
    {
      MinViews = newMinViews * SearchConstants.ViewsMultiplier;
      MaxViews = newMaxViews * SearchConstants.ViewsMultiplier;
    }
  }
}
