import streamlit as st

# Setup for Mobile View
st.set_page_config(page_title="KLK Survey", layout="centered")

# Custom UI for Mobile
st.markdown("""
    <style>
    /* Make buttons bigger for thumb tapping */
    .stButton>button {
        width: 100%;
        height: 3em;
        font-size: 20px !important;
        border-radius: 10px;
    }
    /* Reduce padding for small screens */
    .block-container { padding-top: 1rem; }
    </style>
    """, unsafe_allow_html=True)

st.title("🧪 KLK OLEO Survey")

# Use Expander to save vertical space on mobile
with st.expander("📌 STEP 1: Select Category", expanded=True):
    category = st.radio("Business Segment", ["Personal Care", "Home Care", "Others"], horizontal=True)
    sub_cat = st.selectbox("Product Type", ["Shampoo", "Body Wash", "Detergent", "Dishwash", "Others"])

st.divider()

# Big Camera Button
st.subheader("📸 STEP 2: Capture Photo")
photo = st.camera_input("Scan Ingredients")

if photo:
    st.success("Photo Ready!")
    with st.form("data_form"):
        st.subheader("📝 STEP 3: Verify Details")
        brand = st.text_input("Brand Name")
        origin = st.selectbox("Origin", ["Local (Malaysia)", "Import"])
        
        # Multi-select for Surfactants
        surfactants = st.multiselect("Contains:", ["SLS", "SLES", "MES", "CAPB", "LABSA", "Others"])
        
        notes = st.text_area("Notes/Remarks")
        
        # Large Submit Button
        submit = st.form_submit_button("SAVE TO CLOUD")
        
        if submit:
            st.balloons()
            st.success("Data Uploaded Successfully!")
