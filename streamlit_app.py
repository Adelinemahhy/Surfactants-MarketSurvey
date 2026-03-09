import streamlit as st
import pandas as pd
from PIL import Image

# Page Configuration
st.set_page_config(page_title="KLK Market Survey Tool", page_icon="🧪", layout="centered")

# Custom CSS for a cleaner mobile look
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; font-weight: bold; }
    .stSelectbox { margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🧪 KLK OLEO Market Survey")
st.info("Automated Data Entry for Surfactants Research")

# 1. Primary Category Selection
main_category = st.selectbox("Select Business Segment", ["Personal Care", "Home Care", "Others"])

# 2. Sub-category Logic
sub_category = ""
if main_category == "Personal Care":
    sub_category = st.radio("Product Type", ["Shampoo", "Body Wash", "Hand Wash"])
elif main_category == "Home Care":
    sub_category = st.radio("Product Type", ["Liquid Detergent", "Powder Detergent", "Dishwash Liquid"])
else:
    sub_category = st.text_input("Specify Product (e.g., Dry Shampoo, Dishwash Paste)")

st.divider()

# 3. Camera Input
st.subheader("📸 Capture Product Image")
captured_photo = st.camera_input("Take a photo of the ingredients or front label")

if captured_photo:
    st.success("Photo captured successfully!")
    
    # Placeholder for AI OCR Logic (Coming in Step 3)
    with st.expander("📝 Review & Edit Extracted Data", expanded=True):
        brand = st.text_input("Brand")
        product_name = st.text_input("Product Name", value=sub_category)
        
        col1, col2 = st.columns(2)
        with col1:
            importer = st.text_input("Importer")
            manufacturer = st.text_input("Manufacturer")
            distributor = st.text_input("Distributor")
        
        with col2:
            origin_type = st.selectbox("Local or Import", ["Local", "Import"])
            country = st.text_input("Country of Origin")
            
        ingredients = st.text_area("Ingredients List")
        
        # Surfactants Detection (Multi-select)
        surfactants_list = ["SLS", "SLES", "MES", "CAPB", "LABSA", "CDEA", "Others"]
        detected = st.multiselect("Detected Surfactants", surfactants_list)
        
        notes = st.text_area("Additional Notes")

        # Submit Button
        if st.button("Save to Database"):
            st.balloons()
            st.success("Data synced to cloud! (Connecting to Google Sheets in next step)")
