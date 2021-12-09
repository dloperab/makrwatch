using MakrwatchClient.Models;

namespace MakrwatchClient.Services.Contracts
{
  public interface ILocationService
  {
    List<Location> GetLocations();
    Location GetLocationByCode(string countryCode);
  }
}
