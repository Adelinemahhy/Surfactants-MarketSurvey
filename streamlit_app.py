import streamlit as st
import os
import base64

st.set_page_config(
    page_title="KLK Market Survey",
    page_icon="🌿",
    layout="centered"
)

# Helper: encode image to base64 for inline display
def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap');

    .stApp { background-color: #FFFFFF !important; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}

    .block-container {
        max-width: 400px !important;
        padding-top: 0 !important;
        padding-left: 1.2rem !important;
        padding-right: 1.2rem !important;
    }

    body, p, div, label, span {
        font-family: 'DM Sans', sans-serif !important;
    }

    /* ── Logo banner ── */
    .logo-banner {
        background-color: #065F46;
        border-radius: 0 0 20px 20px;
        padding: 24px 32px 20px 32px;
        text-align: center;
        margin-bottom: 28px;
    }
    .logo-banner img {
        height: 56px;
        width: auto;
        display: inline-block;
    }
    .logo-subtitle {
        font-family: 'DM Sans', sans-serif;
        font-size: 11px;
        letter-spacing: 3px;
        color: rgba(167,243,208,0.75);
        text-transform: uppercase;
        margin-top: 8px;
    }

    /* ── Page text ── */
    .page-title {
        text-align: center;
        font-size: 22px;
        font-weight: 700;
        color: #065F46;
        margin-bottom: 4px;
        font-family: 'DM Sans', sans-serif;
    }
    .page-sub {
        text-align: center;
        font-size: 13px;
        color: #9CA3AF;
        margin-bottom: 28px;
        font-family: 'DM Sans', sans-serif;
    }

    /* ── Buttons: all same size, centred ── */
    div[data-testid="stButton"] {
        display: flex !important;
        justify-content: center !important;
    }

    div.stButton > button {
        width: 300px !important;
        min-width: 300px !important;
        max-width: 300px !important;
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
        transition: background-color 0.2s ease !important;
        margin: 0 auto 12px auto !important;
    }

    div.stButton > button:hover {
        background-color: #047857 !important;
        box-shadow: 0 6px 16px rgba(6,95,70,0.3) !important;
    }

    /* ── Back: plain text, not a pill ── */
    .back-btn div[data-testid="stButton"] {
        justify-content: flex-start !important;
    }
    .back-btn div.stButton > button {
        width: auto !important;
        min-width: unset !important;
        max-width: unset !important;
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
        margin: 0 0 16px 0 !important;
        text-decoration: underline !important;
    }
    .back-btn div.stButton > button:hover {
        background-color: transparent !important;
        color: #065F46 !important;
        box-shadow: none !important;
    }

    /* ── Form inputs ── */
    .stTextInput > label, .stTextArea > label {
        font-family: 'DM Sans', sans-serif !important;
        font-size: 13px !important;
        font-weight: 500 !important;
        color: #374151 !important;
    }
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        border-radius: 12px !important;
        border: 1.5px solid #D1FAE5 !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 14px !important;
        color: #111827 !important;
    }
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #059669 !important;
        box-shadow: 0 0 0 2px rgba(5,150,105,0.12) !important;
    }

    .stCameraInput > label {
        font-family: 'DM Sans', sans-serif !important;
        font-size: 12px !important;
        color: #6B7280 !important;
    }
    .streamlit-expanderHeader {
        font-family: 'DM Sans', sans-serif !important;
        color: #065F46 !important;
        font-size: 13px !important;
    }
    .stSuccess { border-radius: 12px !important; }
    [data-testid="column"] { padding: 0 5px !important; }
    </style>
""", unsafe_allow_html=True)

# ── STATE ──
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# ── LOGO BANNER (shown on both pages) ──
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
            <div style='color:white; font-family:DM Sans,sans-serif; font-weight:700;
                        font-size:20px; letter-spacing:3px;'>KLK OLEO</div>
            <div class='logo-subtitle'>Surfactants Division</div>
        </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════
# PAGE A: HOME
# ══════════════════════════════
if st.session_state.page == 'home':

    st.markdown("<div class='page-title'>Market Survey</div>", unsafe_allow_html=True)
    st.markdown("<div class='page-sub'>Select a product category</div>", unsafe_allow_html=True)

    if st.button("PERSONAL CARE"):
        st.session_state.category = "Personal Care"
        st.session_state.page = 'capture'
        st.rerun()

    if st.button("HOME CARE"):
        st.session_state.category = "Home Care"
        st.session_state.page = 'capture'
        st.rerun()

    if st.button("OTHERS"):
        st.session_state.category = "Others"
        st.session_state.page = 'capture'
        st.rerun()

# ══════════════════════════════
# PAGE B: CAPTURE
# ══════════════════════════════
elif st.session_state.page == 'capture':

    st.markdown("<div class='back-btn'>", unsafe_allow_html=True)
    if st.button("← Back to categories", key="back"):
        st.session_state.page = 'home'
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(f"<div class='page-title'>{st.session_state.category}</div>", unsafe_allow_html=True)
    st.markdown("<div class='page-sub'>Fill in the product details below</div>", unsafe_allow_html=True)

    st.markdown("**📸 Photos**")
    c1, c2 = st.columns(2)
    with c1:
        photo1 = st.camera_input("Front")
    with c2:
        photo2 = st.camera_input("Back")
    with st.expander("+ Add side angle"):
        photo3 = st.camera_input("Side")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("**📝 Product Info**")
    brand = st.text_input("Brand Name", placeholder="e.g. Dove, Sunlight…")
    notes = st.text_area("Observations", placeholder="Ingredients, claims, packaging notes…", height=100)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("SUBMIT"):
        st.balloons()
        st.success("✓ Saved successfully!")
