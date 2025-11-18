# ThirdPartyWebsites_Analyzer
Created for a university assignment, checks the percentage of third-party websites contacted when visiting the top 25 websites.
## Dependencies
- Pandas
- Matplotlib
## Slicing:

urls["domain"] = urls["url"].apply(
    lambda u: urlparse(u).hostname.split(".")[-2] if urlparse(u).hostname else None
)
✅ How it works
- urlparse(u).hostname → extracts the hostname from the URL. "https://oauthaccountmanager.googleapis.com/v1/" → "oauthaccountmanager.googleapis.com"
- if urlparse(u).hostname else None → safely handles malformed URLs or missing hostnames.

This will give you a new column domain containing exactly what you want.