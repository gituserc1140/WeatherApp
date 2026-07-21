import streamlit as st
import requests

def fetch_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def main():
    st.title("Weather App")
    api_key = st.text_input("Enter your OpenWeatherMap API Key:")
    city = st.text_input("Enter city name:")
    if st.button("Get Weather") and api_key and city:
        weather_data = fetch_weather(api_key, city)
        if weather_data.get("cod") == 200:
            st.write(f"City: {weather_data['name']}")
            st.write(f"Temperature: {weather_data['main']['temp']}°C")
            st.write(f"Weather: {weather_data['weather'][0]['description']}")
            st.write(f"Humidity: {weather_data['main']['humidity']}%")
            st.write(f"Wind Speed: {weather_data['wind']['speed']} m/s")
        else:
            st.error("City not found or API key is invalid.")

if __name__ == "__main__":
    main()