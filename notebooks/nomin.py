import sys 
import requests
import json
params = {"q":sys.argv[1], "format":"jsonv2"}
response = requests.get("https://nominatim.openstreetmap.org/search.php", params=params)
#print(response.json())

display_name = response.json()[0]['display_name']
type = response.json()[0]['type']
lat = response.json()[0]['lat']
lon = response.json()[0]['lon'] 

print(display_name)
print(f'Type:{type}')
print(f'Latitude:{lat}')
print(f'Longitude:{lon}')
