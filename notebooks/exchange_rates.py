import sys
import requests
import json
url = "https://api.frankfurter.app/2024-01-01..2024-01-10"
params = {"base":"USD", "symbols":"INR"}
data = requests.get(url, params=params)

amount = data.json()['amount']
base = data.json()['base']
start_date = data.json()['start_date']
end_date = data.json()['end_date']
rates = data.json()['rates']

print(amount)
print(base)
print(start_date)
print(end_date)
print(rates)
