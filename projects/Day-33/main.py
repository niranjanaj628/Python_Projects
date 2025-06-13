import requests
from datetime import datetime

# response = requests.get(url="https://open-notify.org/Open-Notify-API/ISS-Location-Now/")
# response.raise_for_status()

# data = response.json()

# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']

# iss_position = (latitude, longitude)
# print(iss_position)

my_lat = 19.07
my_lng = 72.87
 
parameteres = {"lat" : my_lat, 
               "lng" : my_lng,
               "formatted" : 0
              }

response = requests.get("https://api.sunrise-sunset.org/json" , params= parameteres)
response.raise_for_status()

data = response.json()
# print(data)

sunrise = data['results']['sunrise'].split('T')[1].split(":")[0]
sunset = data['results']['sunset'].split('T')[1].split(":")[0]

print('sunrise:' ,sunrise)
print('sunset:' ,sunset)
time_now = datetime.now()
print(f'Time now: {time_now.hour}')