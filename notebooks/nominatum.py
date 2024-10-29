import sys 
import requests
import json
params = {"q":sys.argv[1], "format":"jsonv2"}
data = requests.get("https://nominatim.openstreetmap.org/search.php", params=params).json()

for match in data: 
    print(data['display_name'])
    print(data['type'])
    print(data['lat'])
    print(data['lon'])
          
