# Weather App

A real-time weather application built with [Streamlit](https://streamlit.io/) and the [OpenWeatherMap](https://openweathermap.org/) API. Enter any city name and instantly see the current temperature, weather condition, humidity, wind speed, and more — all in a clean, dark-themed UI.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://weatherapp-8keslrcnbnbebcmkigqg2w.streamlit.app/)
[![GitHub](https://img.shields.io/badge/GitHub-WeatherApp-24292e?logo=github&style=flat-square)](https://github.com/gituserc1140/WeatherApp)
[![Sponsor me on GitHub](https://img.shields.io/badge/Sponsor%20me%20on-GitHub-EA4AAA?logo=githubsponsors&style=flat-square)](https://github.com/sponsors/gituserc1140)

## About

This app lets you check live weather data for any city around the world. It uses the free OpenWeatherMap Current Weather API and displays:

- 🌡️ Temperature (current, feels-like, min, max)
- 📋 Weather condition with an emoji icon
- 💧 Humidity
- 💨 Wind speed
- 🌍 City name and country

Your API key is entered securely via the sidebar (password-masked) and is **never stored or logged**.

## Getting started

### Prerequisites

- Python 3.8+
- A free [OpenWeatherMap API key](https://home.openweathermap.org/users/sign_up)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/gituserc1140/WeatherApp.git
   cd WeatherApp
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

## API key setup

You can provide your `OPENWEATHERMAP_API_KEY` in any of these ways (in order of priority):

| Method | How |
|---|---|
| **Sidebar input** | Paste your key into the sidebar field at runtime (recommended for quick use) |
| **Streamlit secrets** | Add `OPENWEATHERMAP_API_KEY = "your_key"` to `.streamlit/secrets.toml` |
| **Environment variable** | `export OPENWEATHERMAP_API_KEY=your_key` before running |

> **Note:** Your API key is always treated as a password — it is masked in the UI and never logged.

## How to use

1. Open the app in your browser (it starts automatically after `streamlit run app.py`).
2. Enter your OpenWeatherMap API key in the **sidebar** (only needed once per session).
3. Type a **city name** in the main input field (e.g. `London`, `Tokyo`, `New York`).
4. Click **Get Weather** to fetch and display the current conditions.

## Notes

- Keep your API key secure and never commit it to source control.
- The free OpenWeatherMap tier allows up to 1,000 API calls per day.
