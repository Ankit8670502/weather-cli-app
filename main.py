from fastapi import FastAPI
import requests

app = FastAPI(title="Weather API", version="1.0")

def fetch_weather(latitude: float, longitude: float):
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}"
        f"&current=temperature_2m,wind_speed_10m"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "Failed to fetch weather"}

    data = response.json()

    temp = data["current"]["temperature_2m"]
    windspeed = data["current"]["wind_speed_10m"]

    if windspeed < 10:
        condition = "Calm"
    elif 10 <= windspeed < 20:
        condition = "Breezy"
    else:
        condition = "Windy"

    return {
        "temperature": temp,
        "wind_speed": windspeed,
        "wind_condition": condition,
        "unit": "Celsius"
    }


@app.get("/")
def home():
    return {"message": "Weather API is running 🚀"}


@app.get("/weather")
def get_weather(latitude: float, longitude: float):
    return fetch_weather(latitude, longitude)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
