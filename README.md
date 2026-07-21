# ✨ Compliment Generator

[![View on GitHub](https://img.shields.io/badge/GitHub-View%20on%20GitHub-181717?style=for-the-badge&logo=github)](https://github.com/gituserc1140/WeatherApp)
[![Sponsor](https://img.shields.io/badge/Sponsor-%E2%9D%A4-ea4aaa?style=for-the-badge&logo=github-sponsors)](https://github.com/sponsors/gituserc1140)

A Streamlit app that instantly generates a short, personalised compliment powered by OpenAI. Enter a few details about yourself and receive a warm, heartfelt message in seconds.

---

## Features

- 🔑 Enter your own OpenAI API key directly in the app — no server-side secrets needed
- ✨ Generates a unique, personalised compliment based on your name and details
- 🎨 Beautiful gradient UI with a responsive layout
- 🔗 GitHub and GitHub Sponsors buttons built into the interface

---

## Prerequisites

- Python 3.9+
- An [OpenAI API key](https://platform.openai.com/api-keys)

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/gituserc1140/WeatherApp.git
   cd WeatherApp
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## Running the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

---

## How to Use

1. **Enter your OpenAI API key** in the sidebar on the left.  
   Get a key at <https://platform.openai.com/api-keys>.
2. **Type your name** in the *Your name* field.
3. **Add a few details** about yourself — hobbies, recent achievements, anything you like.
4. Click **✨ Generate My Compliment** and enjoy your personalised message!

---

## Optional: Pre-configure the API Key

If you prefer not to enter the key every time, you can configure it via:

- **Streamlit secrets** — create `.streamlit/secrets.toml`:

  ```toml
  OPENAI_API_KEY = "sk-..."
  ```

- **Environment variable**:

  ```bash
  export OPENAI_API_KEY="sk-..."
  ```

When a pre-configured key is detected the sidebar input can be left blank.

---

## Notes

- Keep your API key secure and never commit it to version control.
- The app uses the `gpt-4o-mini` model for fast, cost-effective generation.