using MakrwatchClient.Models;
using MakrwatchClient.Services.Contracts;

namespace MakrwatchClient.Services
{
  public class LocationService : ILocationService
  {
    private List<Location> _locations = new();

    public List<Location> GetLocations()
    {
      var flagUrlRoot = "images/flags/{0}.png";
      _locations = new List<Location>
      {
        new Location("BH", "United Arab Emirates", string.Format(flagUrlRoot, "bh")),
        new Location("EG", "Egypt", string.Format(flagUrlRoot, "eg")),
        new Location("IL", "Israel", string.Format(flagUrlRoot, "il")),
        new Location("NL", "Netherlands", string.Format(flagUrlRoot, "nl")),
        new Location("CA", "Canada", string.Format(flagUrlRoot, "ca")),
        new Location("CO", "Colombia", string.Format(flagUrlRoot, "co")),
        new Location("NZ", "New Zealand", string.Format(flagUrlRoot, "nz")),
        new Location("AU", "Australia", string.Format(flagUrlRoot, "au")),
        new Location("ES", "Spain", string.Format(flagUrlRoot, "es")),
        new Location("RU", "Russia", string.Format(flagUrlRoot, "ru")),
        new Location("FR", "France", string.Format(flagUrlRoot, "fr")),
        new Location("PT", "Portugal", string.Format(flagUrlRoot, "pt")),
        new Location("US", "United States", string.Format(flagUrlRoot, "us")),
        new Location("GB", "United Kingdom", string.Format(flagUrlRoot, "gb")),
        new Location("MX", "Mexico", string.Format(flagUrlRoot, "mx")),
        new Location("BR", "Brazil", string.Format(flagUrlRoot, "br")),
        new Location("IN", "India", string.Format(flagUrlRoot, "in"))
      };

      _locations = _locations.OrderBy(x => x.Name).ToList();

      return _locations;
    }

    public Location GetLocationByCode(string countryCode)
    {
      var location = _locations.SingleOrDefault(x => x.Code.Equals(countryCode));
      if (location == null)
      {
        location = Location.GetUnknown(countryCode);
      }

      return location;
    }
  }
}
