import requests

response = requests.get(url="https://open-notify.org/Open-Notify-API/ISS-Location-Now/")
response.raise_for_status()

data = response.json()

longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']

iss_position = (latitude, longitude)
print(iss_position)
