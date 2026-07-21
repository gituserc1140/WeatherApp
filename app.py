import os

import requests
import streamlit as st

_CSS = """
<style>
/* ── Page background ───────────────────────────────────────────── */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0a1628, #1a3a5c, #0d2137);
    min-height: 100vh;
}
[data-testid="stHeader"] { background: transparent; }

/* ── Hero banner ───────────────────────────────────────────────── */
.hero {
    text-align: center;
    padding: 2.5rem 1rem 1.5rem;
}
.hero h1 {
    font-size: 2.6rem;
    font-weight: 800;
    background: linear-gradient(90deg, #60c0ff, #38bdf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.3rem;
}
.hero p {
    color: #94c6e8;
    font-size: 1.05rem;
    margin-top: 0;
}

/* ── Weather result card ───────────────────────────────────────── */
.weather-card {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(56,189,248,0.35);
    border-radius: 14px;
    padding: 1.6rem 2rem;
    color: #e2e8f0;
    font-size: 1rem;
    line-height: 2;
    margin-top: 1rem;
}
.weather-card .city-name {
    font-size: 1.5rem;
    font-weight: 700;
    color: #38bdf8;
    margin-bottom: 0.5rem;
}
.weather-label {
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #38bdf8;
    margin-bottom: 0.4rem;
}

/* ── Error card ────────────────────────────────────────────────── */
.error-card {
    background: rgba(239,68,68,0.12);
    border: 1px solid rgba(239,68,68,0.45);
    border-radius: 14px;
    padding: 1.2rem 1.6rem;
    color: #fca5a5;
    font-size: 0.97rem;
    margin-top: 1rem;
}

/* ── Buttons ───────────────────────────────────────────────────── */
[data-testid="stButton"] button {
    background: linear-gradient(135deg, #0ea5e9, #0284c7) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.45rem 1.2rem !important;
    font-weight: 600 !important;
    transition: opacity 0.2s !important;
}
[data-testid="stButton"] button:hover { opacity: 0.85 !important; }

/* ── Sidebar ───────────────────────────────────────────────────── */
[data-testid="stSidebar"] {
    background: rgba(10,22,40,0.90);
    border-right: 1px solid rgba(56,189,248,0.2);
}
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] div { color: #cbd5e1 !important; }
[data-testid="stSidebar"] h2 {
    color: #38bdf8 !important;
    font-size: 1.1rem;
}

/* ── Warning / info text ───────────────────────────────────────── */
[data-testid="stAlert"] p { color: #ffffff !important; }
[data-testid="stSpinner"] p { color: #7dd3fc !important; }
</style>
"""

WEATHER_ICONS = {
    "clear sky": "☀️",
    "few clouds": "🌤️",
    "scattered clouds": "⛅",
    "broken clouds": "🌥️",
    "overcast clouds": "☁️",
    "light rain": "🌦️",
    "moderate rain": "🌧️",
    "heavy intensity rain": "⛈️",
    "thunderstorm": "⛈️",
    "snow": "❄️",
    "mist": "🌫️",
    "fog": "🌫️",
    "haze": "🌫️",
}


def weather_icon(description: str) -> str:
    desc_lower = description.lower()
    for key, icon in WEATHER_ICONS.items():
        if key in desc_lower:
            return icon
    return "🌡️"


def get_configured_api_key() -> str:
    if "OPENWEATHERMAP_API_KEY" in st.secrets:
        return st.secrets["OPENWEATHERMAP_API_KEY"]
    return os.getenv("OPENWEATHERMAP_API_KEY", "")


def fetch_weather(api_key: str, city: str) -> dict:
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
    }
    response = requests.get(base_url, params=params, timeout=10)
    return response.json()


def main():
    st.set_page_config(
        page_title="Weather App",
        page_icon="🌤️",
        layout="centered",
    )
    st.markdown(_CSS, unsafe_allow_html=True)

    # ── Hero header ────────────────────────────────────────────────
    st.markdown(
        """
        <div class="hero">
            <h1>🌤️ Weather App</h1>
            <p>Get real-time weather information for any city in the world.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Sidebar ────────────────────────────────────────────────────
    st.sidebar.header("Settings")
    api_key_input = st.sidebar.text_input(
        "OpenWeatherMap API Key",
        type="password",
        help="Enter your API key here, or configure OPENWEATHERMAP_API_KEY in Streamlit secrets/environment.",
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown(
        """
        <div style="display:flex; flex-direction:column; gap:0.5rem;">
            <a href="https://github.com/gituserc1140/WeatherApp" target="_blank"
               style="display:inline-flex; align-items:center; gap:0.4rem; background:#24292e;
                      color:#fff; padding:0.4rem 0.9rem; border-radius:6px; text-decoration:none;
                      font-size:0.85rem; font-weight:600;">
                <img src="https://github.com/favicon.ico" width="16" height="16" alt=""/>
                View on GitHub
            </a>
            <a href="https://github.com/sponsors/gituserc1140" target="_blank"
               style="display:inline-flex; align-items:center; gap:0.4rem; background:#bf3989;
                      color:#fff; padding:0.4rem 0.9rem; border-radius:6px; text-decoration:none;
                      font-size:0.85rem; font-weight:600;">
                ❤️ Sponsor on GitHub
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

    stripped_api_key = api_key_input.strip()
    api_key = stripped_api_key if stripped_api_key else get_configured_api_key()

    if not api_key:
        st.warning("Please enter your OpenWeatherMap API key in the sidebar to continue.")
        st.stop()

    # ── Main content ───────────────────────────────────────────────
    city = st.text_input("🏙️ Enter city name:", placeholder="e.g. London, Tokyo, New York")

    if st.button("Get Weather") and city.strip():
        with st.spinner("Fetching weather data… ☁️"):
            weather_data = fetch_weather(api_key, city.strip())

        if weather_data.get("cod") == 200:
            main_data = weather_data["main"]
            wind_data = weather_data["wind"]
            description = weather_data["weather"][0]["description"]
            icon = weather_icon(description)
            city_name = weather_data["name"]
            country = weather_data["sys"]["country"]

            st.markdown('<div class="weather-label">🌍 Current Weather</div>', unsafe_allow_html=True)
            st.markdown(
                f"""
                <div class="weather-card">
                    <div class="city-name">{icon} {city_name}, {country}</div>
                    <div>🌡️ <strong>Temperature:</strong> {main_data['temp']}°C
                         (feels like {main_data['feels_like']}°C)</div>
                    <div>📋 <strong>Condition:</strong> {description.capitalize()}</div>
                    <div>💧 <strong>Humidity:</strong> {main_data['humidity']}%</div>
                    <div>💨 <strong>Wind Speed:</strong> {wind_data['speed']} m/s</div>
                    <div>🔼 <strong>Max Temp:</strong> {main_data['temp_max']}°C
                         &nbsp;|&nbsp; 🔽 <strong>Min Temp:</strong> {main_data['temp_min']}°C</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            message = weather_data.get("message", "Unknown error.")
            st.markdown(
                f'<div class="error-card">⚠️ {message.capitalize()}</div>',
                unsafe_allow_html=True,
            )


if __name__ == "__main__":
    main()