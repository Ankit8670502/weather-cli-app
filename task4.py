import requests
try:
    url="https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    response=requests.get(url)

    if response.status_code==500:
        print("Server error")
    elif response.status_code==400:
        print("Bad request")
    elif response.status_code==200:
        print("Api working!")
        data=response.json()
        t=data["hourly"]["time"]
        temp=data["hourly"]["temperature_2m"]
        humidity=data["hourly"]["relative_humidity_2m"]
        wind=data["hourly"]["wind_speed_10m"]
        print(t[:5],temp[:5],humidity[:5],wind[:5])
    else:
        print("Something went wrong")
except requests.exceptions.ConnectionError:
    print("No internet connection")
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.RequestException:
    print("Some request error occured")
