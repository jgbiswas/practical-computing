import sys
import requests
url = "https://api.dictionaryapi.dev/api/v2/entries/en"
params = {"text":sys.argv[1]}
output = requests.get(url, params=params).text
print(output)
