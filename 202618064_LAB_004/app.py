# import streamlit as st
# import pandas as pd
# import joblib

# # Load the trained pipeline
# model = joblib.load("airbnb_price_pipeline.pkl")

# # Page configuration
# st.set_page_config(
#     page_title="Airbnb Price Predictor",
#     page_icon="🏠",
#     layout="centered"
# )

# # Title
# st.title("🏠 Airbnb Price Predictor")
# st.write("Enter the listing details below to estimate the nightly Airbnb price.")

# st.divider()

# # Input fields
# neighbourhood_group = st.selectbox(
#     "Neighbourhood Group",
#     ["Manhattan", "Brooklyn", "Queens", "Bronx", "Staten Island"]
# )

# neighbourhood = st.text_input(
#     "Neighbourhood",
#     placeholder="e.g. Midtown"
# )

# room_type = st.selectbox(
#     "Room Type",
#     ["Entire home/apt", "Private room", "Shared room"]
# )

# latitude = st.number_input(
#     "Latitude",
#     value=40.7128,
#     format="%.4f"
# )

# longitude = st.number_input(
#     "Longitude",
#     value=-74.0060,
#     format="%.4f"
# )

# minimum_nights = st.number_input(
#     "Minimum Nights",
#     min_value=1,
#     value=3,
#     step=1
# )

# number_of_reviews = st.number_input(
#     "Number of Reviews",
#     min_value=0,
#     value=10,
#     step=1
# )

# reviews_per_month = st.number_input(
#     "Reviews per Month",
#     min_value=0.0,
#     value=1.0,
#     step=0.1
# )

# calculated_host_listings_count = st.number_input(
#     "Host Listings Count",
#     min_value=1,
#     value=1,
#     step=1
# )

# availability_365 = st.number_input(
#     "Availability (365 days)",
#     min_value=0,
#     max_value=365,
#     value=180,
#     step=1
# )

# st.divider()

# # Prediction button
# if st.button("💰 Predict Airbnb Price", use_container_width=True):

#     # Create input DataFrame with exact feature names
#     input_data = pd.DataFrame({
#         "neighbourhood_group": [neighbourhood_group],
#         "neighbourhood": [neighbourhood],
#         "latitude": [latitude],
#         "longitude": [longitude],
#         "room_type": [room_type],
#         "minimum_nights": [minimum_nights],
#         "number_of_reviews": [number_of_reviews],
#         "reviews_per_month": [reviews_per_month],
#         "calculated_host_listings_count": [calculated_host_listings_count],
#         "availability_365": [availability_365]
#     })

#     # Make prediction
#     prediction = model.predict(input_data)[0]

#     # Display result
#     st.success(
#         f"Estimated Nightly Price: **${prediction:.2f}**"
#     )

#     st.caption(
#         "Prediction generated using the trained Random Forest machine learning pipeline."
#     )

import streamlit as st
import pandas as pd
import joblib

# --------------------------------------------------
# Load trained pipeline
# --------------------------------------------------
import os
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "airbnb_price_pipeline.pkl")

model = joblib.load(MODEL_PATH)

# --------------------------------------------------
# Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Airbnb Price Intelligence",
    page_icon="🏠",
    layout="wide"
)

# --------------------------------------------------
# Custom CSS
# --------------------------------------------------
st.markdown("""
<style>

    /* ---------- Page ---------- */
    .stApp {
        background: #F5E6EC;
    }

    .block-container {
        max-width: 1100px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* ---------- Header ---------- */
    .hero {
        background: linear-gradient(135deg,#D96C8A, #B94F70);
        padding: 1.8rem 2.3rem;
        border-radius: 20px;
        margin-bottom: 1.5rem;
        box-shadow: 0 10px 28px rgba(101, 88, 245, 0.18);
    }

    .hero-title {
        color: #FFFFFF;
        font-size: 2.25rem;
        font-weight: 800;
        margin: 0;
    }

    .hero-subtitle {
        color: #FFF1F5;
        font-size: 0.95rem;
        margin-top: 0.45rem;
        margin-bottom: 0;
    }

    /* ---------- Section ---------- */
    .section-header {
        margin-top: 1.25rem;
        margin-bottom: 0.7rem;
    }

    .section-title {
        color: #302B4F;
        font-size: 1.15rem;
        font-weight: 750;
        margin-bottom: 0.15rem;
    }

    .section-text {
        color: #77728D;
        font-size: 0.82rem;
        margin: 0;
    }

    /* ---------- Labels ---------- */
    label {
        color: #403A5F !important;
        font-weight: 600 !important;
    }

    /* ---------- Inputs ---------- */
    .stTextInput input,
    .stNumberInput input,
    .stSelectbox div[data-baseweb="select"] {
        border-radius: 10px !important;
    }

    /* ---------- Button ---------- */
    .stButton > button {
        width: 100%;
        background: #C95678;
        color: #FFFFFF;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 1rem;
        font-size: 1rem;
        font-weight: 700;
        margin-top: 1rem;
        box-shadow: 0 6px 16px rgba(201, 86, 120, 0.18);
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        background: #B44769;
        color: #FFFFFF;
        transform: translateY(-1px);
        box-shadow: 0 8px 20px rgba(201, 86, 120, 0.25);
    }
    /* ---------- Prediction ---------- */
        .prediction-card {
        background: linear-gradient(135deg, #4A2936, #613746);
        padding: 1.7rem;
        border-radius: 20px;
        text-align: center;
        margin-top: 1.6rem;
        box-shadow: 0 12px 28px rgba(74, 41, 54, 0.18);
    }

    .prediction-label {
        color: #EFD9E0;
        font-size: 0.82rem;
        font-weight: 600;
        letter-spacing: 1px;
        margin-bottom: 0.25rem;
    }

    .prediction-price {
        color: #FFFFFF;
        font-size: 2.7rem;
        font-weight: 800;
        margin: 0;
    }

    .prediction-note {
        color: #DCC3CC;
        font-size: 0.75rem;
        margin-top: 0.5rem;
    }

    /* ---------- Footer ---------- */
    .footer {
        text-align: center;
        color: #858096;
        font-size: 0.75rem;
        margin-top: 2rem;
        padding-top: 1rem;
        border-top: 1px solid #E2DFEF;
    }

    /* ---------- Hide Streamlit branding ---------- */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Hero
# --------------------------------------------------
st.markdown("""
<div class="hero">
    <div class="hero-title">🏠 Airbnb Price Intelligence</div>
    <p class="hero-subtitle">
        Machine-learning powered nightly price estimation for New York City listings
    </p>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Location
# --------------------------------------------------
st.markdown("""
<div class="section-header">
    <div class="section-title">📍 Location</div>
    <p class="section-text">
        Enter the geographical details of the Airbnb listing.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    neighbourhood_group = st.selectbox(
        "Neighbourhood Group",
        ["Manhattan", "Brooklyn", "Queens", "Bronx", "Staten Island"]
    )

with col2:
    neighbourhood = st.text_input(
        "Neighbourhood",
        placeholder="e.g. Midtown"
    )

col1, col2 = st.columns(2)

with col1:
    latitude = st.number_input(
        "Latitude",
        value=40.7128,
        format="%.4f"
    )

with col2:
    longitude = st.number_input(
        "Longitude",
        value=-74.0060,
        format="%.4f"
    )

# --------------------------------------------------
# Property
# --------------------------------------------------
st.markdown("""
<div class="section-header">
    <div class="section-title">🏡 Property</div>
    <p class="section-text">
        Specify the accommodation type and minimum stay.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    room_type = st.selectbox(
        "Room Type",
        ["Entire home/apt", "Private room", "Shared room"]
    )

with col2:
    minimum_nights = st.number_input(
        "Minimum Nights",
        min_value=1,
        value=3,
        step=1
    )

# --------------------------------------------------
# Listing Activity
# --------------------------------------------------
st.markdown("""
<div class="section-header">
    <div class="section-title">📊 Listing Activity</div>
    <p class="section-text">
        Add review activity and annual availability information.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    number_of_reviews = st.number_input(
        "Number of Reviews",
        min_value=0,
        value=10,
        step=1
    )

with col2:
    reviews_per_month = st.number_input(
        "Reviews per Month",
        min_value=0.0,
        value=1.0,
        step=0.1
    )

col1, col2 = st.columns(2)

with col1:
    calculated_host_listings_count = st.number_input(
        "Host Listings Count",
        min_value=1,
        value=1,
        step=1
    )

with col2:
    availability_365 = st.number_input(
        "Availability (365 days)",
        min_value=0,
        max_value=365,
        value=180,
        step=1
    )

# --------------------------------------------------
# Prediction
# --------------------------------------------------
if st.button("💰  ESTIMATE  PRICE"):

    input_data = pd.DataFrame({
        "neighbourhood_group": [neighbourhood_group],
        "neighbourhood": [neighbourhood],
        "latitude": [latitude],
        "longitude": [longitude],
        "room_type": [room_type],
        "minimum_nights": [minimum_nights],
        "number_of_reviews": [number_of_reviews],
        "reviews_per_month": [reviews_per_month],
        "calculated_host_listings_count": [calculated_host_listings_count],
        "availability_365": [availability_365]
    })

    prediction = model.predict(input_data)[0]

    st.markdown(f"""
    <div class="prediction-card">
        <div class="prediction-label">ESTIMATED NIGHTLY PRICE</div>
        <div class="prediction-price">${prediction:,.2f}</div>
        <div class="prediction-note">
            Prediction generated using the tuned Random Forest pipeline
        </div>
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("""
<div class="footer">
    
</div>Airbnb Price Prediction
""", unsafe_allow_html=True)