import sys
import requests
import json
url = "https://api.dictionaryapi.dev/api/v2/entries/en/compassion"
print(requests.get(url).json())
