import sys
import requests
import json
url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
data = requests.get(url).json()
print(data)
