import streamlit as st
import os
import base64

st.set_page_config(
    page_title="Market Survey",
    page_icon="KLKOLEO Logo",
    layout="centered"
)

def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Inject PWA tags so "Add to Homescreen" uses the correct icon & title
if os.path.exists("KLKOLEO Logo"):
    _icon_b64 = img_to_base64("KLKOLEO Logo")
    st.markdown(f"""
        <link rel="manifest" href="manifest.json">
        <meta name="apple-mobile-web-app-capable" content="yes">
        <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
        <meta name="apple-mobile-web-app-title" content="KLK Survey">
        <link rel="apple-touch-icon" href="data:image/png;base64,{_icon_b64}">
        <meta name="theme-color" content="#016836">
    """, unsafe_allow_html=True)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap');

    html, body, .stApp {
        background-color: #016836 !important;
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
        background-color: #016836;
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

    /* Titles */
    .page-title {
        text-align: center;
        font-size: 22px;
        font-weight: 700;
        color: #016836;
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

    /* Buttons */
    div[data-testid="stButton"] {
        display: flex !important;
        justify-content: center !important;
    }
    div.stButton > button {
        width: 320px !important;
        height: 60px !important;
        border-radius: 50px !important;
        border: none !important;
        background-color: #016836 !important;
        color: #FFFFFF !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 14px !important;
        font-weight: 700 !important;
        letter-spacing: 1.5px !important;
        text-transform: uppercase !important;
        box-shadow: 0 4px 12px rgba(6,95,70,0.2) !important;
        margin: 0 auto !important;
    }
    div.stButton > button:hover {
        background-color: #047857 !important;
    }

    /* Camera labels */
    .stCameraInput > label {
        font-family: 'DM Sans', sans-serif !important;
        font-size: 12px !important;
        color: #016836 !important;
    }

    .streamlit-expanderHeader {
        font-family: 'DM Sans', sans-serif !important;
        color: #016836 !important;
    }
    .stSuccess { border-radius: 12px !important; }
    [data-testid="column"] { padding: 0 5px !important; }

    .section-lbl {
        font-size: 12px;
        font-weight: 700;
        color: #374151;
        letter-spacing: 1px;
        margin-bottom: 10px;
        padding: 0 20px;
        font-family: 'DM Sans', sans-serif;
    }
    .form-wrap { padding: 0 20px 40px 20px; }
    </style>
""", unsafe_allow_html=True)

# ── STATE ──
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'category' not in st.session_state:
    st.session_state.category = ''

# ── LOGO BANNER ──
logo_path = "KLKOLEO Logo"
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
    st.markdown("<p style='text-align:center;font-size:10px;color:#E5E7EB;letter-spacing:2px;font-family:DM Sans,sans-serif;'>KUALA LUMPUR KEPONG BERHAD</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;font-size:11px;color:#D1D5DB;font-family:DM Sans,sans-serif;margin-top:4px;'>© Adeline Mah</p>", unsafe_allow_html=True)


# ══════════════════════════════
# PAGE B: CAPTURE
# ══════════════════════════════
elif st.session_state.page == 'capture':

    if st.button("← Back", key="back"):
        st.session_state.page = 'home'
        st.rerun()

    st.markdown(f"<div class='page-title'>{st.session_state.category}</div>", unsafe_allow_html=True)
    st.markdown("<div class='page-sub'>Take photos of the product</div>", unsafe_allow_html=True)

    st.markdown("<div class='form-wrap'>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        photo1 = st.camera_input("Front")
    with c2:
        photo2 = st.camera_input("Back")

    with st.expander("+ Add side angle"):
        photo3 = st.camera_input("Side")

    st.markdown("<br>", unsafe_allow_html=True)

    _, col, _ = st.columns([1, 2, 1])
    with col:
        if st.button("SUBMIT", use_container_width=True):
            st.balloons()
            st.success("✓ Saved successfully!")

    st.markdown("</div>", unsafe_allow_html=True)
