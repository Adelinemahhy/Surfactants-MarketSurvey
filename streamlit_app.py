import streamlit as st
import os

# 1. PAGE SETUP
st.set_page_config(
    page_title="Market Survey", 
    page_icon="icon.png", 
    layout="centered"
)

# 2. THE ULTIMATE UI DESIGN (CSS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@700;800&display=swap');

    /* 1. Full Screen Green Background */
    .stApp {
        background-color: #065F46 !important; /* KLK Deep Green */
    }

    /* 2. Hide all Streamlit UI clutter */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display:none;}
    .block-container { padding-top: 2rem; }

    /* 3. Typography */
    .brand-logo {
        width: 100px;
        margin-left: 20px;
    }
    .main-title {
        font-family: 'Poppins', Aptos;
        color: #FFFFFF;
        text-align: center;
        font-size: 70px;
        font-weight: 800;
        letter-spacing: 1px;
        margin-top: 20px;
        margin-bottom: 40px;
        text-transform: uppercase;
    }

    /* 4. The Pill Buttons (Large & Rounded) */
    div.stButton > button {
        width: 100%;
        height: 140px !important; /* Extra large for thumb tapping */
        border-radius: 70px !important; /* Perfect Pill Shape */
        border: none !important;
        background-color: #D1DED8 !important; /* Soft Light Grey-Green from your draft */
        color: #065F46 !important; /* Text color matches background */
        font-family: 'Poppins', sans-serif !important;
        font-size: 70px !important;
        font-weight: 700 !important;
        letter-spacing: 1px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        transition: 0.3s ease;
        margin-bottom: 10px;
    }
    
    div.stButton > button:hover {
        background-color: #FFFFFF !important;
        transform: scale(1.02);
    }

    /* 5. Back Button (Capture Page) */
    .back-btn button {
        height: auto !important;
        width: auto !important;
        background: transparent !important;
        color: #FFFFFF !important;
        text-decoration: underline !important;
        font-size: 16px !important;
        box-shadow: none !important;
        border-radius: 0 !important;
    }
    
    /* 6. Form Styling (Capture Page) */
    .stTextInput input {
        border-radius: 15px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. APP LOGIC & STATE
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# --- PAGE A: HOME SCREEN (Matches your Draft) ---
if st.session_state.page == 'home':
    # Logo Placeholder
    if os.path.exists("logo.png"):
        st.image("logo.png", width=80)
    else:
        st.markdown("<p style='color:white; margin-left:25px; font-weight:bold;'>KLK OLEO</p>", unsafe_allow_html=True)
    
    st.markdown("<h1 class='main-title'>MARKET SURVEY</h1>", unsafe_allow_html=True)
    
    # Large Pill Buttons
    st.markdown("<div style='padding: 0 30px;'>", unsafe_allow_html=True)
    
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
        
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Bottom Subtext
    st.markdown("<p style='text-align:center; color:#A7F3D0; font-size:10px; margin-top:50px; opacity:0.6;'>SURFACTANTS | ADELINE MAH</p>", unsafe_allow_html=True)

# --- PAGE B: CAPTURE PAGE ---
elif st.session_state.page == 'capture':
    # Back button at the top
    if st.button("← Back to Categories", key="back"):
        st.session_state.page = 'home'
        st.rerun()

    st.markdown(f"<h2 style='color:white; text-align:center;'>{st.session_state.category}</h2>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown("<div style='background:white; padding:20px; border-radius:30px; margin: 0 10px;'>", unsafe_allow_html=True)
        
        st.subheader("📸 Step 1: Scan")
        c1, c2 = st.columns(2)
        with c1:
            photo1 = st.camera_input("Front View")
        with c2:
            photo2 = st.camera_input("Back View")
            
        with st.expander("➕ Extra Angle"):
            photo3 = st.camera_input("Side View")

        if st.button("🚀 SUBMIT DATA"):
            st.balloons()
            st.success("Saved to Cloud!")
            # Future Google Sheets Sync Here
        
        st.markdown("</div>", unsafe_allow_html=True)
