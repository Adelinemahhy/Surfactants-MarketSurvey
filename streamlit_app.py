import streamlit as st
import os

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="Market Survey", 
    page_icon="KLK Oleo Logo.png", 
    layout="centered"
)

# 2. BRANDING & CUSTOM TYPOGRAPHY (Poppins & Aptos)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600;800&display=swap');

    /* Global Typography: Aptos for body, Poppins for headers */
    html, body, [class*="st-"] {
        font-family: 'Aptos', 'Segoe UI', Roboto, sans-serif;
    }
    h1, h2, h3, .tile-text {
        font-family: 'Poppins', sans-serif !important;
    }

    /* Hide Browser & Streamlit UI for "App-like" feel */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display:none;}
    .block-container { padding: 0rem; }

    /* KLK Deep Green Header Block */
    .klk-header {
        background-color: #065F46; 
        width: 100%;
        padding: 50px 20px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    .klk-header h1 {
        color: #FFFFFF;
        font-size: 32px;
        margin: 0;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .klk-header p {
        color: #A7F3D0;
        font-size: 14px;
        margin-top: 5px;
        font-style: italic;
    }

    /* Home Screen Tiles (The 3 Big Buttons) */
    .tile-container {
        padding: 0 25px;
        display: flex;
        flex-direction: column;
        gap: 20px;
    }
    
    /* Specific styling for the 3 Entry Tiles */
    .stButton > button {
        width: 100%;
        border-radius: 20px;
        transition: 0.3s ease;
    }
    
    .home-tile button {
        height: 120px !important;
        background-color: #FFFFFF !important;
        border: 1.5px solid #E5E7EB !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.06) !important;
        font-family: 'Poppins', sans-serif !important;
        font-size: 20px !important;
        color: #065F46 !important;
    }
    .home-tile button:hover {
        background-color: #065F46 !important;
        color: #FFFFFF !important;
        border-color: #065F46 !important;
        transform: translateY(-3px);
    }

    /* Back Button Styling (Minimalist) */
    .back-btn-container {
        padding: 15px 25px 0 25px;
    }
    .back-btn button {
        background-color: transparent !important;
        border: none !important;
        color: #6B7280 !important;
        text-decoration: underline !important;
        font-size: 15px !important;
        padding: 0 !important;
        height: auto !important;
    }

    /* Page Content Padding */
    .page-content { padding: 0 25px; }
    </style>
    """, unsafe_allow_html=True)

# 3. STATE MANAGEMENT (Page Navigation)
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'selected_cat' not in st.session_state:
    st.session_state.selected_cat = None

# --- PAGE A: HOME (The 3 Tiles) ---
if st.session_state.page == 'home':
    st.markdown("""
        <div class="klk-header">
            <h1>MARKET SURVEY</h1>
            <p>KLK OLEO • SURFACTANTS MARKET SURVEY</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<div class='tile-container'>", unsafe_allow_html=True)
    st.write("### 📂 Choose Segment")
    
    with st.container():
        st.markdown('<div class="home-tile">', unsafe_allow_html=True)
        if st.button("🧴 PERSONAL CARE", key="btn_pc"):
            st.session_state.selected_cat = "Personal Care"
            st.session_state.page = 'capture'
            st.rerun()
            
        if st.button("🏠 HOME CARE", key="btn_hc"):
            st.session_state.selected_cat = "Home Care"
            st.session_state.page = 'capture'
            st.rerun()
            
        if st.button("🧩 OTHERS", key="btn_ot"):
            st.session_state.selected_cat = "Others"
            st.session_state.page = 'capture'
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- PAGE B: CAPTURE PAGE (Drawer-style entry) ---
elif st.session_state.page == 'capture':
    # Top Back Button
    st.markdown('<div class="back-btn-container">', unsafe_allow_html=True)
    if st.button("← Back to Categories", key="back_btn"):
        st.session_state.page = 'home'
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(f"<h2 style='color:#065F46; text-align:center; font-family:Poppins;'>{st.session_state.selected_cat}</h2>", unsafe_allow_html=True)
    
    st.markdown("<div class='page-content'>", unsafe_allow_html=True)
    st.divider()

    # MULTI-PHOTO SECTION (Front & Back Required)
    st.subheader("📸 Step 1: Photos")
    st.caption("Capture at least 2 photos (Front & Back/Ingredients)")
    
    c1, c2 = st.columns(2)
    with c1:
        photo_front = st.camera_input("Front (Brand)")
    with c2:
        photo_back = st.camera_input("Back (Ingredients)")
    
    # Extra Photo Expander (For curved bottles/Side labels)
    with st.expander("➕ Add more angles? (Side/Details)"):
        photo_extra = st.camera_input("Extra Detail Photo")

    if photo_front and photo_back:
        st.success("Core images ready!")
        
        st.subheader("📝 Step 2: Data Entry")
        brand = st.text_input("Brand", placeholder="e.g. KLK Choice")
        p_name = st.text_input("Product Name", placeholder="e.g. Shower Gel 500ml")
        
        # Surfactant List based on Business Intelligence requirements
        surfactant_list = ["SLS", "SLES", "MES", "CAPB", "LABSA", "CDEA", "Others"]
        selected_surfactants = st.multiselect("Contains Surfactants:", surfactant_list)
        
        notes = st.text_area("Additional Remarks (Price, Volume, etc.)")

        # Submission Button
        if st.button("🚀 SAVE TO CLOUD", use_container_width=True):
            st.balloons()
            st.toast("Recording data to KLK central database...", icon="☁️")
            # GOOGLE SHEETS CONNECTION LOGIC GOES HERE
    
    st.markdown("</div>", unsafe_allow_html=True)

# 5. CORPORATE FOOTER
st.markdown("<br><p style='text-align:center; color:#9CA3AF; font-family:Aptos; font-size:10px;'>SURFACTANTS • ADELINE MAH</p>", unsafe_allow_html=True)
