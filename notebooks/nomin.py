import sys 
import requests
import json
params = {"q":sys.argv[1], "format":"jsonv2"}
response = requests.get("https://nominatim.openstreetmap.org/search.php", params=params)

for match in response: 
    print(response['display_name'])
    print(response['type'])
    print(response['lat'])
    print(response['lon'])
          
