using MakrwatchClient.Infrastructure;

namespace MakrwatchClient.Models
{
  public class Location
  {
    public Location(string code, string name, string flagUrl)
    {
      Code = code;
      Name = name;
      FlagUrl = flagUrl;
    }

    public string Code { get; set; }
    public string Name { get; set; }
    public string FlagUrl { get; set; }

    public static Location GetUnknown(string code) => new Location(code, code, Constants.FlagNoneUrl);
  }
}
