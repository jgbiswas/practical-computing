import sys
import requests
url = "https://api.dictionaryapi.dev/api/v2/entries/en/hello"
print(requests.get(url).text)
