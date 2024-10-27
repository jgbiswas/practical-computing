import sys
import requests
import json
url = "https://api.frankfurter.app/2024-01-01..2024-01-10"
params = {"base":"USD", "symbols":"INR"}
data = requests.get(url, params=params).json()
print(data)
for k in data:
    print(k)
