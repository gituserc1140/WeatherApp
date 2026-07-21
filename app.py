import os

import openai
import streamlit as st

GITHUB_REPO_URL = "https://github.com/gituserc1140/WeatherApp"
GITHUB_SPONSORS_URL = "https://github.com/sponsors/gituserc1140"

_CSS = """
<style>
/* ── Page background ───────────────────────────────────────────── */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
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
    background: linear-gradient(90deg, #f9a8d4, #fbcfe8, #fde68a);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.3rem;
}
.hero p {
    color: #cbd5e1;
    font-size: 1.05rem;
    margin-top: 0;
}

/* ── Social buttons ────────────────────────────────────────────── */
.social-buttons {
    display: flex;
    justify-content: center;
    gap: 0.75rem;
    flex-wrap: wrap;
    margin: 0.75rem 0 1.5rem;
}
.social-buttons a {
    text-decoration: none;
}
.social-buttons img {
    height: 28px;
    border-radius: 6px;
    transition: opacity 0.2s;
}
.social-buttons img:hover { opacity: 0.8; }

/* ── Compliment card ────────────────────────────────────────────── */
.compliment-card {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(249,168,212,0.4);
    border-radius: 16px;
    padding: 1.8rem 2rem;
    color: #fce7f3;
    font-size: 1.25rem;
    font-weight: 500;
    line-height: 1.7;
    text-align: center;
    margin-top: 1.2rem;
}
.compliment-label {
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #f9a8d4;
    margin-bottom: 0.4rem;
    text-align: center;
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

/* ── Main button ───────────────────────────────────────────────── */
[data-testid="stButton"] button {
    background: linear-gradient(135deg, #be185d, #7c3aed) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.5rem 1.4rem !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    transition: opacity 0.2s !important;
    width: 100% !important;
}
[data-testid="stButton"] button:hover { opacity: 0.85 !important; }

/* ── Sidebar ───────────────────────────────────────────────────── */
[data-testid="stSidebar"] {
    background: rgba(15,12,41,0.85);
    border-right: 1px solid rgba(249,168,212,0.2);
}
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] div { color: #cbd5e1 !important; }
[data-testid="stSidebar"] h2 {
    color: #f9a8d4 !important;
    font-size: 1.1rem;
}

/* ── Input fields ──────────────────────────────────────────────── */
[data-testid="stTextInput"] input,
[data-testid="stTextArea"] textarea {
    background: rgba(255,255,255,0.06) !important;
    border: 1px solid rgba(249,168,212,0.3) !important;
    border-radius: 8px !important;
    color: #f1f5f9 !important;
}

/* ── Warning / info text ────────────────────────────────────────── */
[data-testid="stAlert"] p { color: #ffffff !important; }
[data-testid="stSpinner"] p { color: #f9a8d4 !important; }
</style>
"""

_SYSTEM_PROMPT = (
    "You are a warm, uplifting compliment generator. "
    "When given information about a person, you craft a short (2–4 sentences), "
    "genuine, and personalised compliment that makes them feel special. "
    "Be sincere, positive, and avoid generic platitudes."
)


def get_configured_api_key() -> str:
    if "OPENAI_API_KEY" in st.secrets:
        return st.secrets["OPENAI_API_KEY"]
    return os.getenv("OPENAI_API_KEY", "")


def generate_compliment(api_key: str, name: str, details: str) -> dict:
    client = openai.OpenAI(api_key=api_key)
    user_message = f"Person's name: {name}\nDetails about them: {details}"
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": _SYSTEM_PROMPT},
                {"role": "user", "content": user_message},
            ],
            max_tokens=200,
            temperature=0.9,
        )
        return {"text": response.choices[0].message.content.strip(), "has_error": False}
    except openai.AuthenticationError:
        return {"text": "Invalid API key. Please check your OpenAI API key and try again.", "has_error": True}
    except openai.RateLimitError:
        return {"text": "Rate limit reached. Please wait a moment and try again.", "has_error": True}
    except openai.OpenAIError as exc:
        return {"text": f"OpenAI error: {exc}", "has_error": True}


def main():
    st.set_page_config(
        page_title="Compliment Generator",
        page_icon="✨",
        layout="centered",
    )
    st.markdown(_CSS, unsafe_allow_html=True)

    # ── Hero header ────────────────────────────────────────────────
    st.markdown(
        """
        <div class="hero">
            <h1>✨ Compliment Generator</h1>
            <p>Enter a few details and receive a personalised, heartfelt compliment instantly.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Social buttons ─────────────────────────────────────────────
    st.markdown(
        f"""
        <div class="social-buttons">
            <a href="{GITHUB_REPO_URL}" target="_blank">
                <img src="https://img.shields.io/badge/GitHub-View%20on%20GitHub-181717?style=for-the-badge&logo=github" alt="View on GitHub">
            </a>
            <a href="{GITHUB_SPONSORS_URL}" target="_blank">
                <img src="https://img.shields.io/badge/Sponsor-%E2%9D%A4-ea4aaa?style=for-the-badge&logo=github-sponsors" alt="Sponsor on GitHub">
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Sidebar ────────────────────────────────────────────────────
    st.sidebar.header("Settings")
    api_key_input = st.sidebar.text_input(
        "OpenAI API Key",
        type="password",
        help="Enter your OpenAI API key here. Get one at https://platform.openai.com/api-keys",
    )
    stripped_api_key = api_key_input.strip()
    api_key = stripped_api_key if stripped_api_key else get_configured_api_key()

    if not api_key:
        st.warning("Please enter your OpenAI API key in the sidebar to continue.")
        st.stop()

    # ── Main form ──────────────────────────────────────────────────
    name = st.text_input("Your name", placeholder="e.g. Alex")
    details = st.text_area(
        "Tell us a little about yourself",
        placeholder="e.g. I love hiking, just finished a big project at work, and I'm learning guitar.",
        height=120,
    )

    if st.button("✨ Generate My Compliment"):
        if not name.strip():
            st.warning("Please enter your name so we can personalise your compliment.")
        else:
            with st.spinner("Crafting your compliment… ✨"):
                result = generate_compliment(api_key, name.strip(), details.strip())

            if result["has_error"]:
                st.markdown(
                    f'<div class="error-card">⚠️ {result["text"]}</div>',
                    unsafe_allow_html=True,
                )
            else:
                st.markdown('<div class="compliment-label">💌 Your Compliment</div>', unsafe_allow_html=True)
                st.markdown(
                    f'<div class="compliment-card">{result["text"]}</div>',
                    unsafe_allow_html=True,
                )


if __name__ == "__main__":
    main()