import streamlit as st
import os

# 1. PAGE SETUP (The "Identity")
st.set_page_config(
    page_title="KLK Survey Pro", 
    page_icon="icon.png", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. THE "APP-IFY" MAGIC (Hiding Browser UI & Adding Branding)
st.markdown("""
    <head>
        <meta name="apple-mobile-web-app-capable" content="yes">
        <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    </head>
    <style>
    /* 1. Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display:none;}
    
    /* 2. Global Clean Look */
    .stApp { background-color: #FFFFFF; }
    .block-container { padding-top: 2rem; padding-bottom: 5rem; }

    /* 3. KLK Branding Colors */
    :root { --klk-green: #065F46; }

    /* 4. Custom Header */
    .brand-header {
        text-align: center;
        margin-bottom: 25px;
    }
    .brand-title {
        color: #065F46;
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        font-size: 28px;
        margin: 0;
    }
    .brand-sub {
        color: #6B7280;
        font-size: 13px;
        letter-spacing: 1px;
    }

    /* 5. Mobile-First Buttons (The Tiles) */
    div.stButton > button {
        width: 100%;
        height: 85px;
        border-radius: 18px;
        border: 1.5px solid #F3F4F6;
        background-color: #F9FAFB;
        color: #374151;
        font-weight: 600;
        font-size: 16px !important;
        transition: 0.2s ease;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }
    div.stButton > button:hover {
        border-color: #065F46;
        background-color: #ECFDF5;
        color: #065F46;
        transform: translateY(-2px);
    }
    
    /* 6. Input Field Styling */
    .stTextInput input, .stSelectbox div {
        border-radius: 12px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. TOP LOGO & TITLE
with st.container():
    # Attempt to load Logo
    if os.path.exists("logo.png"):
        col_l, col_r = st.columns([1, 4])
        with col_l:
            st.image("logo.png", width=70)
        with col_r:
            st.markdown("<div class='brand-header'><h1 class='brand-title'>KLK OLEO</h1><p class='brand-sub'>SURFACTANTS SURVEY</p></div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='brand-header'><h1 class='brand-title'>KLK OLEO</h1><p class='brand-sub'>SURFACTANTS SURVEY</p></div>", unsafe_allow_html=True)

# 4. APP NAVIGATION TILES
st.markdown("### 📂 Choose Segment")
c1, c2 = st.columns(2)
with c1:
    if st.button("🧴\nPersonal Care"):
        st.session_state.segment = "Personal Care"
with c2:
    if st.button("🏠\nHome Care"):
        st.session_state.segment = "Home Care"

# Show Selection Status
if 'segment' in st.session_state:
    st.info(f"Selected: **{st.session_state.segment}**")

st.divider()

# 5. DATA CAPTURE SECTION
st.subheader("📸 Step 1: Scan Product")
photo = st.camera_input("Ingredients Scan")

if photo:
    st.success("Image Ready!")
    with st.expander("📝 Step 2: Confirm Details", expanded=True):
        brand = st.text_input("Brand", placeholder="e.g., Dove")
        prod_name = st.text_input("Product Name", placeholder="e.g., Deep Moisture Body Wash")
        
        # Surfactant List for KLK Focus
        surfactants = st.multiselect("Surfactants Found:", ["SLS", "SLES", "MES", "CAPB", "LABSA", "Others"])
        
        origin = st.radio("Origin:", ["Local (MY)", "Imported"], horizontal=True)
        
        # Submission Button
        if st.button("🚀 SAVE TO CLOUD"):
            st.balloons()
            st.toast("Syncing with KLK Database...", icon="☁️")
            # Logic for Google Sheets will be added here next!

# 6. APP FOOTER (Internal Notice)
st.markdown("<br><p style='text-align:center; color:#9CA3AF; font-size:10px;'>FOR INTERNAL USE ONLY • KLK OLEO BI TEAM</p>", unsafe_allow_html=True)
