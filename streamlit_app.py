import streamlit as st
import os

# 1. PAGE SETUP
st.set_page_config(
    page_title="KLK Market Survey",
    page_icon="🌿",
    layout="centered"
)

# 2. PREMIUM UI DESIGN
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@300;400;500&display=swap');

    /* === BASE === */
    .stApp {
        background-color: #0A3D2B !important;
        background-image:
            radial-gradient(ellipse 80% 60% at 50% -20%, rgba(16,185,100,0.18) 0%, transparent 70%),
            radial-gradient(ellipse 50% 40% at 90% 80%, rgba(6,95,70,0.3) 0%, transparent 60%);
        min-height: 100vh;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display:none;}
    .block-container {
        padding-top: 3rem !important;
        padding-bottom: 3rem !important;
        max-width: 520px !important;
    }

    /* === HOME PAGE === */
    .klk-eyebrow {
        font-family: 'DM Sans', sans-serif;
        font-size: 11px;
        font-weight: 500;
        letter-spacing: 4px;
        color: #6EE7B7;
        text-align: center;
        text-transform: uppercase;
        margin-bottom: 6px;
        opacity: 0.8;
    }

    .klk-headline {
        font-family: 'Syne', sans-serif;
        font-size: 48px;
        font-weight: 800;
        color: #FFFFFF;
        text-align: center;
        line-height: 1.0;
        letter-spacing: -1px;
        margin-bottom: 8px;
    }

    .klk-sub {
        font-family: 'DM Sans', sans-serif;
        font-size: 14px;
        color: rgba(167, 243, 208, 0.6);
        text-align: center;
        margin-bottom: 48px;
        letter-spacing: 0.5px;
    }

    .divider {
        height: 1px;
        background: linear-gradient(to right, transparent, rgba(110,231,183,0.3), transparent);
        margin: 0 30px 40px 30px;
    }

    .section-label {
        font-family: 'DM Sans', sans-serif;
        font-size: 11px;
        letter-spacing: 3px;
        color: rgba(167,243,208,0.5);
        text-transform: uppercase;
        text-align: center;
        margin-bottom: 20px;
    }

    /* === PILL BUTTONS (HOME) === */
    div.stButton > button {
        width: 100% !important;
        height: 80px !important;
        border-radius: 100px !important;
        border: 1.5px solid rgba(110, 231, 183, 0.2) !important;
        background: rgba(255,255,255,0.06) !important;
        color: #FFFFFF !important;
        font-family: 'Syne', sans-serif !important;
        font-size: 16px !important;
        font-weight: 700 !important;
        letter-spacing: 2px !important;
        text-transform: uppercase !important;
        backdrop-filter: blur(12px) !important;
        transition: all 0.25s ease !important;
        margin-bottom: 12px !important;
    }

    div.stButton > button:hover {
        background: rgba(110, 231, 183, 0.15) !important;
        border-color: rgba(110, 231, 183, 0.6) !important;
        color: #6EE7B7 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 12px 32px rgba(0,0,0,0.25), 0 0 0 1px rgba(110,231,183,0.15) !important;
    }

    div.stButton > button:active {
        transform: translateY(0px) !important;
    }

    /* === CAPTURE PAGE CARD === */
    .capture-card {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(110, 231, 183, 0.15);
        border-radius: 24px;
        padding: 32px 28px;
        backdrop-filter: blur(20px);
    }

    .step-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(110, 231, 183, 0.12);
        border: 1px solid rgba(110, 231, 183, 0.25);
        border-radius: 100px;
        padding: 6px 16px;
        font-family: 'DM Sans', sans-serif;
        font-size: 12px;
        font-weight: 500;
        color: #6EE7B7;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-bottom: 16px;
    }

    .capture-title {
        font-family: 'Syne', sans-serif;
        font-size: 28px;
        font-weight: 800;
        color: #FFFFFF;
        margin-bottom: 28px;
        line-height: 1.1;
    }

    /* === FORM INPUTS === */
    .stTextInput > label,
    .stTextArea > label {
        font-family: 'DM Sans', sans-serif !important;
        font-size: 12px !important;
        letter-spacing: 2px !important;
        text-transform: uppercase !important;
        color: rgba(167, 243, 208, 0.7) !important;
        font-weight: 500 !important;
    }

    .stTextInput > div > div > input {
        background: rgba(255,255,255,0.07) !important;
        border: 1px solid rgba(110,231,183,0.2) !important;
        border-radius: 14px !important;
        color: #FFFFFF !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 15px !important;
        padding: 14px 18px !important;
    }

    .stTextInput > div > div > input:focus {
        border-color: rgba(110,231,183,0.55) !important;
        box-shadow: 0 0 0 3px rgba(110,231,183,0.08) !important;
    }

    .stTextArea > div > div > textarea {
        background: rgba(255,255,255,0.07) !important;
        border: 1px solid rgba(110,231,183,0.2) !important;
        border-radius: 14px !important;
        color: #FFFFFF !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 15px !important;
    }

    /* === SUBMIT BUTTON OVERRIDE === */
    .submit-btn > div > button {
        background: linear-gradient(135deg, #059669, #065F46) !important;
        border: none !important;
        color: #FFFFFF !important;
        height: 64px !important;
        font-size: 14px !important;
        letter-spacing: 3px !important;
        box-shadow: 0 8px 24px rgba(5,150,105,0.35) !important;
    }

    .submit-btn > div > button:hover {
        background: linear-gradient(135deg, #10B981, #059669) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 12px 32px rgba(5,150,105,0.5) !important;
    }

    /* === BACK LINK === */
    .back-link > div > button {
        height: auto !important;
        background: transparent !important;
        border: none !important;
        color: rgba(167,243,208,0.6) !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 13px !important;
        font-weight: 400 !important;
        letter-spacing: 1px !important;
        padding: 0 !important;
        box-shadow: none !important;
        text-decoration: underline !important;
        text-transform: none !important;
    }

    .back-link > div > button:hover {
        color: #6EE7B7 !important;
        transform: none !important;
        background: transparent !important;
        border: none !important;
    }

    /* Camera widget labels */
    .stCameraInput > label {
        font-family: 'DM Sans', sans-serif !important;
        font-size: 12px !important;
        letter-spacing: 1.5px !important;
        text-transform: uppercase !important;
        color: rgba(167,243,208,0.7) !important;
    }

    /* Expander */
    .streamlit-expanderHeader {
        color: rgba(167,243,208,0.7) !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 13px !important;
    }

    /* Success message */
    .stSuccess {
        background: rgba(5,150,105,0.2) !important;
        border: 1px solid rgba(110,231,183,0.3) !important;
        border-radius: 14px !important;
        color: #6EE7B7 !important;
    }

    /* Column gaps */
    [data-testid="column"] {
        padding: 0 6px !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. STATE INIT
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# ─────────────────────────────────────────────
# PAGE A: HOME
# ─────────────────────────────────────────────
if st.session_state.page == 'home':

    st.markdown("<br>", unsafe_allow_html=True)

    # Logo
    if os.path.exists("logo.png"):
        col_l, col_c, col_r = st.columns([1, 2, 1])
        with col_c:
            st.image("logo.png", width=72)
    else:
        st.markdown("<p style='text-align:center; font-family:Syne,sans-serif; color:#6EE7B7; font-size:13px; letter-spacing:4px;'>KLK OLEO</p>", unsafe_allow_html=True)

    st.markdown("<div class='klk-eyebrow'>Surfactants Division</div>", unsafe_allow_html=True)
    st.markdown("<div class='klk-headline'>MARKET<br>SURVEY</div>", unsafe_allow_html=True)
    st.markdown("<div class='klk-sub'>Select a product category to begin</div>", unsafe_allow_html=True)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.markdown("<div class='section-label'>Choose Category</div>", unsafe_allow_html=True)

    st.markdown("<div style='padding: 0 16px;'>", unsafe_allow_html=True)

    if st.button("✦  PERSONAL CARE"):
        st.session_state.category = "Personal Care"
        st.session_state.page = 'capture'
        st.rerun()

    if st.button("✦  HOME CARE"):
        st.session_state.category = "Home Care"
        st.session_state.page = 'capture'
        st.rerun()

    if st.button("✦  OTHERS"):
        st.session_state.category = "Others"
        st.session_state.page = 'capture'
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-family:DM Sans,sans-serif; font-size:10px; color:rgba(110,231,183,0.25); letter-spacing:3px;'>KUALA LUMPUR KEPONG BERHAD</p>", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# PAGE B: CAPTURE
# ─────────────────────────────────────────────
elif st.session_state.page == 'capture':

    st.markdown("<br>", unsafe_allow_html=True)

    col_back, col_space = st.columns([1, 3])
    with col_back:
        st.markdown("<div class='back-link'>", unsafe_allow_html=True)
        if st.button("← Back", key="back"):
            st.session_state.page = 'home'
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Card
    st.markdown("<div class='capture-card'>", unsafe_allow_html=True)

    st.markdown(f"<div class='step-badge'>📍 {st.session_state.category}</div>", unsafe_allow_html=True)
    st.markdown("<div class='capture-title'>Product<br>Capture</div>", unsafe_allow_html=True)

    # STEP 1: Photos
    st.markdown("<div class='section-label' style='text-align:left; margin-bottom:12px;'>Step 01 — Photograph</div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        photo1 = st.camera_input("Front View")
    with c2:
        photo2 = st.camera_input("Back View")

    with st.expander("+ Add extra angle"):
        photo3 = st.camera_input("Side View")

    st.markdown("<br>", unsafe_allow_html=True)

    # STEP 2: Info
    st.markdown("<div class='section-label' style='text-align:left; margin-bottom:12px;'>Step 02 — Product Info</div>", unsafe_allow_html=True)

    brand = st.text_input("Brand Name", placeholder="e.g. Dove, Sunlight, Palmolive…")
    notes = st.text_area("Observations", placeholder="Key ingredients, claims, packaging notes…", height=110)

    st.markdown("<br>", unsafe_allow_html=True)

    # Submit
    st.markdown("<div class='submit-btn'>", unsafe_allow_html=True)
    if st.button("SUBMIT DATA  →"):
        st.balloons()
        st.success("✓  Entry saved successfully")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)  # close capture-card
