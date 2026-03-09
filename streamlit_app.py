import streamlit as st

# 1. Page Configuration for Mobile
st.set_page_config(page_title="Surfactants MarketSurvey", , layout="centered")

# 2. Custom CSS for "App-like" Visuals
st.markdown("""
    <style>
    /* Background and Font */
    .stApp {
        background-color: #F0F2F6;
    }
    /* Style the buttons to look like App Tiles */
    div.stButton > button {
        width: 100%;
        height: 100px;
        border-radius: 20px;
        border: none;
        background-color: #FFFFFF;
        color: #1E3A8A; /* Dark Blue */
        font-weight: bold;
        font-size: 18px !important;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #1E3A8A;
        color: white;
        transform: translateY(-3px);
    }
    /* Header Styling */
    .main-header {
        text-align: center;
        color: #1E3A8A;
        font-family: 'Helvetica', sans-serif;
        margin-bottom: 0px;
    }
    .sub-header {
        text-align: center;
        color: #6B7280;
        font-size: 14px;
        margin-bottom: 30px;
    }
    /* Form Container */
    .data-card {
        background
