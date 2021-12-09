
namespace MakrwatchClient.Helpers
{
  public class NumberHelpers
  {
    public static string GetShortText(int num)
    {
      if (num > 999999999 || num < -999999999)
      {
        return num.ToString("0,,,.###B");
      }
      else if (num > 999999 || num < -999999)
      {
        return num.ToString("0,,.##M");
      }
      else if (num > 999 || num < -999)
      {
        return num.ToString("0,.#K");
      }

      return num.ToString();
    }
  }
}
