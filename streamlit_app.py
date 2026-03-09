import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="KLK Market Survey", page_icon="🧪")

st.title("🧪 KLK OLEO Market Survey")
st.info("Internship Project: Automated Product Data Entry")

# 2. Main Categories
main_category = st.selectbox("Select Business Segment", ["Personal Care", "Home Care", "Others"])

# 3. Sub-categories
sub_category = ""
if main_category == "Personal Care":
    sub_category = st.radio("Product Type", ["Shampoo", "Body Wash", "Hand Wash"])
elif main_category == "Home Care":
    sub_category = st.radio("Product Type", ["Liquid Detergent", "Powder Detergent", "Dishwash Liquid"])
else:
    sub_category = st.text_input("Specify Product (e.g., Dry Shampoo)")

st.divider()

# 4. Camera Feature
st.subheader("📸 Capture Photo")
img_file = st.camera_input("Take a photo of the product label or ingredients")

if img_file:
    st.success("Photo captured successfully!")
    
    with st.expander("📝 Review & Edit Information", expanded=True):
        brand = st.text_input("Brand")
        product = st.text_input("Product Name", value=sub_category if sub_category else "")
        manufacturer = st.text_input("Manufacturer")
        ingredients = st.text_area("Ingredients")
        
        if st.button("Confirm & Save Data"):
            st.balloons()
            st.write("Data recorded! (Next: Connecting to Google Sheets)")
