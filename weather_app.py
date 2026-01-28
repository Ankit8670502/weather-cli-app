import requests
import json
import os
def get_weather(latitude, longitude):
    try:
        url=f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
        response=requests.get(url)
        if response.status_code==200:
            print("Api Working!!")
            data=response.json()
            temp = data["current"]["temperature_2m"]
            windspeed = data["current"]["wind_speed_10m"]
            time=data["current"]["time"]
            timezone=data["timezone"]
            return temp,windspeed,time,timezone
        else:
            print("Something went wrong")
            return None
    except requests.exceptions.Timeout:
        print("Request timed out")
    except requests.exceptions.ConnectionError:
        print("No internet connection")
    except requests.exceptions.RequestException:
        print("Some request error occured")
    return None
# 👇 MENU STARTS HERE
while True:
    print("\n------ WEATHER CLI APP ------")
    print("1. Get Weather")
    print("2. View History")
    print("3. Exit")
    choice = input("Choose option: ")

    if choice == "1":
        # PUT your current weather logic here
        latitude=float(input("Enter latitude"))
        longitude=float(input("Enter longitude"))
        result=get_weather(latitude,longitude)
        print("---------------Weather Report----------------------------")
        if result is not None:
            temp,windspeed,time,timezone=result
            print(f'''Temperature : {temp}
        Wind Speed : {windspeed}
        Time : {time}
        Timezone : {timezone}''')
        condition=''
        if windspeed<10:
            condition='Calm'
            print(f"Wind Condition : {condition}")
        elif windspeed>10 and windspeed<20:
            condition='Breezy'
            print(f"Wind Condition : {condition}")
        else:
            condition='Windy'
            print(f"Wind Condition : {condition}")
        weather_data={
            "Temperature" : temp,
            "Wind Speed" : windspeed,
            "Time" : time,
            "Timezone" : timezone,
            "Wind Condition" : condition
        }
        file_name = "results.json"

        # Step 1: Load existing data
        if os.path.exists(file_name):
            with open(file_name, "r") as f:
                old_data = json.load(f)
        else:
            old_data = []

        # Step 2: Append new report
        old_data.append(weather_data)

        # Step 3: Save back
        with open(file_name, "w") as f:
            json.dump(old_data, f, indent=4)
        ans=input("Do you want temperature in Fahrenheit? (y/n)")
        f=0
        if ans.lower() in ['y', 'yes']:
            f= ((temp)* (9/5)) + 32
            print(f"Temperature in Fahrenheit : {f}°F")
        pass

    elif choice == "2":

        file_name = "results.json"

        if os.path.exists(file_name):
            with open(file_name, "r") as f:
                history = json.load(f)

            if history:
                print("\n------ WEATHER HISTORY ------")
                for i, record in enumerate(history, start=1):
                    print(f"\nRecord {i}")
                    print(f"Temperature : {record['Temperature']}")
                    print(f"Wind Speed : {record['Wind Speed']}")
                    print(f"Time : {record['Time']}")
                    print(f"Timezone : {record['Timezone']}")
                    print(f"Wind Condition : {record['Wind Condition']}")
            else:
                print("No history found.")

        else:
            print("No history file found.")

            # history logic here later
            pass

    elif choice == "3":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice")




# with open("results.json","w") as f:
#     json.dump(weather_data,f,indent=4)



