import streamlit as st
import os
import base64
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials

st.set_page_config(
    page_title="KLK Market Survey",
    page_icon="KLK_Oleo_Logo.png",
    layout="centered"
)

# ── Helpers ──
def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def save_to_sheets(category, timestamp):
    """Save submission to Google Sheets via st.secrets"""
    try:
        creds = Credentials.from_service_account_info(
            st.secrets["gcp_service_account"],
            scopes=["https://www.googleapis.com/auth/spreadsheets"]
        )
        client = gspread.authorize(creds)
        sheet = client.open("KLK Market Survey").sheet1
        sheet.append_row([timestamp, category])
        return True
    except Exception as e:
        return False

# ── PWA tags ──
if os.path.exists("KLK_Oleo_Logo.png"):
    _icon_b64 = img_to_base64("KLK_Oleo_Logo.png")
    st.markdown(f"""
        <link rel="manifest" href="manifest.json">
        <meta name="apple-mobile-web-app-capable" content="yes">
        <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
        <meta name="apple-mobile-web-app-title" content="KLK Survey">
        <link rel="apple-touch-icon" href="data:image/png;base64,{_icon_b64}">
        <meta name="theme-color" content="#065F46">
    """, unsafe_allow_html=True)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap');

    /* WHITE background */
    html, body, .stApp {
        background-color: #FFFFFF !important;
        font-family: 'DM Sans', sans-serif !important;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}

    .block-container {
        padding: 0 !important;
        margin: 0 auto !important;
        max-width: 420px !important;
    }

    /* Logo banner */
    .logo-banner {
        background-color: #065F46;
        border-radius: 0 0 20px 20px;
        padding: 28px 32px 22px 32px;
        text-align: center;
        margin-bottom: 32px;
        width: 100%;
        box-sizing: border-box;
    }
    .logo-banner img { height: 54px; width: auto; }
    .logo-subtitle {
        font-size: 10px;
        letter-spacing: 3px;
        color: rgba(167,243,208,0.75);
        text-transform: uppercase;
        margin-top: 8px;
        font-family: 'DM Sans', sans-serif;
    }

    /* Titles — dark green on WHITE background, visible */
    .page-title {
        text-align: center;
        font-size: 22px;
        font-weight: 700;
        color: #065F46;
        margin-bottom: 4px;
        padding: 0 20px;
    }
    .page-sub {
        text-align: center;
        font-size: 13px;
        color: #9CA3AF;
        margin-bottom: 28px;
        padding: 0 20px;
    }

    /* Nav buttons (green pills) */
    div[data-testid="stButton"] {
        display: flex !important;
        justify-content: center !important;
    }
    div.stButton > button {
        width: 320px !important;
        height: 60px !important;
        border-radius: 50px !important;
        border: none !important;
        background-color: #065F46 !important;
        color: #FFFFFF !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 14px !important;
        font-weight: 700 !important;
        letter-spacing: 1.5px !important;
        text-transform: uppercase !important;
        box-shadow: 0 4px 12px rgba(6,95,70,0.2) !important;
        margin: 0 auto 12px auto !important;
    }
    div.stButton > button:hover {
        background-color: #047857 !important;
    }

    /* Back button — plain text link */
    .back-btn div[data-testid="stButton"] { justify-content: flex-start !important; }
    .back-btn div.stButton > button {
        width: auto !important;
        min-width: unset !important;
        height: auto !important;
        background-color: transparent !important;
        color: #6B7280 !important;
        border: none !important;
        border-radius: 0 !important;
        box-shadow: none !important;
        font-size: 13px !important;
        font-weight: 400 !important;
        letter-spacing: 0 !important;
        text-transform: none !important;
        padding: 2px 0 !important;
        margin: 0 0 16px 16px !important;
        text-decoration: underline !important;
    }
    .back-btn div.stButton > button:hover {
        background-color: transparent !important;
        color: #065F46 !important;
        box-shadow: none !important;
    }

    /* Camera labels */
    .stCameraInput > label {
        font-family: 'DM Sans', sans-serif !important;
        font-size: 12px !important;
        color: #6B7280 !important;
    }
    .streamlit-expanderHeader {
        font-family: 'DM Sans', sans-serif !important;
        color: #065F46 !important;
    }
    .stSuccess { border-radius: 12px !important; }
    .stWarning { border-radius: 12px !important; }
    [data-testid="column"] { padding: 0 5px !important; }
    .form-wrap { padding: 0 20px 40px 20px; }
    </style>
""", unsafe_allow_html=True)

# ── STATE ──
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'category' not in st.session_state:
    st.session_state.category = ''

# ── LOGO BANNER ──
logo_path = "KLK_Oleo_Logo.png"
if os.path.exists(logo_path):
    logo_b64 = img_to_base64(logo_path)
    st.markdown(f"""
        <div class='logo-banner'>
            <img src='data:image/png;base64,{logo_b64}'/>
            <div class='logo-subtitle'>Surfactants Division</div>
        </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <div class='logo-banner'>
            <div style='color:white;font-family:DM Sans,sans-serif;font-weight:700;
                        font-size:22px;letter-spacing:3px;'>KLK OLEO</div>
            <div class='logo-subtitle'>Surfactants Division</div>
        </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════
# PAGE A: HOME
# ══════════════════════════════
if st.session_state.page == 'home':

    st.markdown("<div class='page-title'>Market Survey</div>", unsafe_allow_html=True)
    st.markdown("<div class='page-sub'>Select a product category</div>", unsafe_allow_html=True)

    _, col, _ = st.columns([1, 2, 1])
    with col:
        if st.button("PERSONAL CARE", use_container_width=True):
            st.session_state.category = "Personal Care"
            st.session_state.page = 'capture'
            st.rerun()
        if st.button("HOME CARE", use_container_width=True):
            st.session_state.category = "Home Care"
            st.session_state.page = 'capture'
            st.rerun()
        if st.button("OTHERS", use_container_width=True):
            st.session_state.category = "Others"
            st.session_state.page = 'capture'
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;font-size:10px;color:#D1D5DB;letter-spacing:2px;font-family:DM Sans,sans-serif;'>KUALA LUMPUR KEPONG BERHAD</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;font-size:11px;color:#D1D5DB;font-family:DM Sans,sans-serif;margin-top:2px;'>© Adeline Mah</p>", unsafe_allow_html=True)


# ══════════════════════════════
# PAGE B: CAPTURE
# ══════════════════════════════
elif st.session_state.page == 'capture':

    # Plain text back link
    st.markdown("<div class='back-btn'>", unsafe_allow_html=True)
    if st.button("← Back", key="back"):
        st.session_state.page = 'home'
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(f"<div class='page-title'>{st.session_state.category}</div>", unsafe_allow_html=True)
    st.markdown("<div class='page-sub'>Take photos of the product</div>", unsafe_allow_html=True)

    st.markdown("<div class='form-wrap'>", unsafe_allow_html=True)

    # Three visible camera inputs
    c1, c2 = st.columns(2)
    with c1:
        photo1 = st.camera_input("Front")
    with c2:
        photo2 = st.camera_input("Back")

    photo3 = st.camera_input("Side (optional)")

    st.markdown("<br>", unsafe_allow_html=True)

    _, col, _ = st.columns([1, 2, 1])
    with col:
        if st.button("SUBMIT", use_container_width=True):
            if not photo1 and not photo2:
                st.warning("⚠️ Please take at least one photo.")
            else:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                saved = save_to_sheets(st.session_state.category, timestamp)
                st.balloons()
                if saved:
                    st.success(f"✓ Saved! {timestamp}")
                else:
                    st.success(f"✓ Submitted at {timestamp}")

    st.markdown("</div>", unsafe_allow_html=True)
