import requests
import json
city="Hyderabad"
url=f"https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
response = requests.get(url)
data=response.json()
#print(data)
with open("readable.json","w") as f:
    js=json.dump(data,f,indent=4)

for col in data:
    if col in ['latitude','longitude','timezone']:
        print(data[col])
curret_temp=data["current"].get("temperature_2m")
current_windspeed=data["current"].get("wind_speed_10m")
current_time=data["current"].get("time")
print(current_time,current_windspeed,curret_temp)