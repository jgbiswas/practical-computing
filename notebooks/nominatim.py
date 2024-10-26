import sys
import requests
import json
url = "https://nominatim.openstreetmap.org/search"
params = {"text":sys.argv[1]}
output = requests.get(url, params=params).text
print(output)
