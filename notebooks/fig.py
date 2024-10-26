import sys
import requests
url = "https://figlet.apps.pipal.in/api/figlet"
params = {"text":sys.argv[1]}
print(requests.get(url, params=params).text)
