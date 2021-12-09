using Microsoft.AspNetCore.Components.Web;
using Microsoft.AspNetCore.Components.WebAssembly.Hosting;

using MakrwatchClient;
using MakrwatchClient.Services.Contracts;
using MakrwatchClient.Services;
using MakrwatchClient.Contracts.V1;

var builder = WebAssemblyHostBuilder.CreateDefault(args);
builder.RootComponents.Add<App>("#app");
builder.RootComponents.Add<HeadOutlet>("head::after");

builder.Services.AddScoped(sp => new HttpClient { BaseAddress = new Uri(ApiRoutes.Root) });
builder.Services.AddScoped<ILocationService, LocationService>();
builder.Services.AddScoped<ISearchVideoService, SearchVideoService>();

await builder.Build().RunAsync();
