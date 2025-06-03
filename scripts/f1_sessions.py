from urllib.request import urlopen
import json
import requests

f1_car_data_url = "https://api.openf1.org/v1/car_data?date>=2025-01-01"
response = requests.get(f1_car_data_url)

print(response.json())