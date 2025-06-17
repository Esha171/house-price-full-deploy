import streamlit as st
import requests
from streamlit_lottie import st_lottie
import json

st.set_page_config(page_title="🏠 House Price Prediction App", page_icon="🏡", layout="centered")

# ---------- HEADER ----------
st.markdown(
    """
    <style>
    .main {
        background-color: #f9f9f9;
    }
    .title {
        text-align: center;
        font-size: 2.5em;
        color: #1f77b4;
        margin-bottom: 0.3em;
    }
    .subtitle {
        text-align: center;
        font-size: 1.2em;
        color: #444;
        margin-bottom: 2em;
    }
    .stButton button {
        background-color: #1f77b4;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="title">🏠 House Price Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Fill out the details below to get a price estimate using our best-trained model.</div>', unsafe_allow_html=True)

# ---------- FORM ----------
with st.form("prediction_form"):
    st.markdown("### 📝 House Details")
    col1, col2 = st.columns(2)

    with col1:
        area = st.number_input("📐 Area (sq.ft)", min_value=100, value=5000, step=100)
        bedrooms = st.slider("🛏 Bedrooms", 1, 10, 3)
        bathrooms = st.slider("🛁 Bathrooms", 1, 10, 2)
        stories = st.slider("🏗 Stories", 1, 4, 1)
        parking = st.slider("🅿 Parking Spaces", 0, 5, 1)

    with col2:
        mainroad = st.radio("🛣 Located on Main Road?", ["No", "Yes"])
        guestroom = st.radio("🛋 Has Guest Room?", ["No", "Yes"])
        basement = st.radio("🏚 Has Basement?", ["No", "Yes"])
        hotwaterheating = st.radio("🔥 Hot Water Heating?", ["No", "Yes"])
        airconditioning = st.radio("❄ Air Conditioning?", ["No", "Yes"])
        prefarea = st.radio("🌟 Preferred Area?", ["No", "Yes"])
        furnishingstatus = st.selectbox("🪑 Furnishing Status", ["Unfurnished", "Semi-Furnished", "Furnished"])

    submit = st.form_submit_button("🔍 Predict Price")

# ---------- BACKEND CALL ----------
if submit:
    st.markdown("🔄 Making prediction...")

    data = {
        "area": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "stories": stories,
        "mainroad": 1 if mainroad == "Yes" else 0,
        "guestroom": 1 if guestroom == "Yes" else 0,
        "basement": 1 if basement == "Yes" else 0,
        "hotwaterheating": 1 if hotwaterheating == "Yes" else 0,
        "airconditioning": 1 if airconditioning == "Yes" else 0,
        "parking": parking,
        "prefarea": 1 if prefarea == "Yes" else 0,
        "furnishingstatus": 0 if furnishingstatus == "Unfurnished" else 1 if furnishingstatus == "Semi-Furnished" else 2,
    }

    try:
        res = requests.post("http://13.232.54.117:8000/predict", json=data)
        result = res.json()

        if "predicted_price" in result:
            st.success(f"💰 **Predicted House Price: ₹{int(result['predicted_price']):,}**")
        else:
            st.error(f"⚠️ Error: {result.get('error', 'Unknown error')}")

    except Exception as e:
        st.error("🚨 Could not connect to the backend API. Please ensure it's running.")
