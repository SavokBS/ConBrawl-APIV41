import brawlstats
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjBlNTA5ZDM1LTk3M2ItNGFmMC05MDkwLTY4MTJiNWY2MTVlZiIsImlhdCI6MTY0MzIwODY0Mywic3ViIjoiZGV2ZWxvcGVyL2MyMzc5MGEyLWE2NjYtOTQ4Zi1mOWQ5LTY1NWFmYzY2NTY5YSIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiNzcuMjQyLjk3LjExIl0sInR5cGUiOiJjbGllbnQifV19.qVxM0eIw9FVNTvsmdFmYRIO4o63NZlsDyCNsdBRB8oeKePu6eho1E9qSmK9x-I4vXJOCHu0RdaglUwDdhv9JXg"
cl = brawlstats.Client(token)
tag = cl.get_profile("8LQ9JR82")
print(tag.brawlers[33].name, tag.brawlers[33].id)
input("")
