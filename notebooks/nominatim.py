import sys
import requests
import json
url = "https://nominatim.openstreetmap.org/search.php"
params = {"q":sys.argv[1], "format":"jsonv2"}
print(requests.get(url, params=params).json())
