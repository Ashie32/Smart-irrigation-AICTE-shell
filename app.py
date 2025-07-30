import streamlit as st
import numpy as np
import joblib


# Load model
model = joblib.load("Farm_irrigation_System.pkl")

# Set page config
st.set_page_config(page_title="Smart Sprinkler System", layout="wide", page_icon="💧")

# Custom CSS
st.markdown("""
    <style>
        .main-title {
            text-align: center;
            font-size: 48px;
            font-weight: bold;
            color: #00BFFF;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            font-size: 20px;
            color: #555;
            margin-bottom: 25px;
        }
        .sprinkler-box {
            border-radius: 15px;
            padding: 15px;
            margin-bottom: 15px;
            text-align: center;
            font-weight: bold;
            font-size: 16px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            transition: 0.3s;
        }
        .sprinkler-box:hover {
            transform: scale(1.03);
        }
        .on {
            background: linear-gradient(to right, #a8e063, #56ab2f);
            color: white;
        }
        .off {
            background: linear-gradient(to right, #ff5858, #f857a6);
            color: white;
        }
        .footer {
            margin-top: 50px;
            padding: 20px;
            text-align: center;
            font-size: 16px;
            color: #aaa;
        }
        .footer a {
            color: #00BFFF;
            text-decoration: none;
            font-weight: bold;
        }
        .stButton > button {
            background: linear-gradient(90deg, #00c6ff, #0072ff);
            color: white;
            font-size: 18px;
            font-weight: bold;
            padding: 0.6em 1.2em;
            border-radius: 10px;
            border: none;
            transition: 0.3s ease-in-out;
        }
        .stButton > button:hover {
            background: linear-gradient(90deg, #0072ff, #00c6ff);
            transform: scale(1.02);
            cursor: pointer;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-title">💧 Smart Sprinkler System 💧</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enter scaled sensor values (0 to 1) to predict sprinkler status</div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2933/2933866.png", width=150)
    st.markdown("### ℹ️ About")
    st.write("This AI-based app uses 20 farm sensor readings to predict ON/OFF status of sprinklers.")
    st.success("🚀 Developed by Ashwani Kumar")

# Sensor Info with Descriptions
sensor_info = [
    ("Soil Moisture 🌱", "Measures water content in the soil"),
    ("Air Humidity 💧", "Relative humidity of the environment"),
    ("Soil Temperature 🌡️", "Soil warmth level"),
    ("Air Temperature ☀️", "Ambient air temperature"),
    ("Nitrogen Level 🧪", "Presence of nitrogen in soil"),
    ("Phosphorus Level 🧪", "Phosphorus content for plant growth"),
    ("Potassium Level 🧪", "Potassium presence for root health"),
    ("Soil pH 🌾", "Acidity or alkalinity of the soil"),
    ("Light Intensity 🔆", "Amount of sunlight received"),
    ("CO₂ Level 🫁", "Carbon dioxide concentration"),
    ("Rainfall Sensor 🌧️", "Detects rainfall or water presence"),
    ("Wind Speed 🌬️", "Airflow speed around the field"),
    ("Leaf Wetness 💦", "Moisture on plant leaves"),
    ("Crop Growth Index 🌿", "AI-estimated growth value"),
    ("Soil Conductivity ⚡", "Soil's electrical conductivity"),
    ("Oxygen Level 🔬", "Dissolved oxygen in soil"),
    ("Soil Texture Index 🪨", "Estimated granularity of soil"),
    ("Fertilizer Residue 🧫", "Remaining nutrients in soil"),
    ("Water Flow Rate 🚿", "Flow rate through irrigation pipes"),
    ("Sunlight Duration ⏳", "Total sunlight exposure today")
]

# Sensor Inputs
sensor_values = []
cols = st.columns(2)
for i, (name, desc) in enumerate(sensor_info):
    with cols[i % 2]:
        val = st.slider(
            f"Sensor {i} - {name}", 0.0, 1.0, 0.5, 0.01,
            help=desc
        )
        sensor_values.append(val)

# Predict
if st.button("Predict Sprinklers"):
    with st.spinner("Analyzing sensor data..."):
        input_array = np.array(sensor_values).reshape(1, -1)
        
        prediction = model.predict(input_array)[0]

    st.markdown("### 🌱 Prediction Results")
    result_cols = st.columns(4)
    for i, status in enumerate(prediction):
        with result_cols[i % 4]:
            st.markdown(
                f"""<div class="sprinkler-box {'on' if status == 1 else 'off'}">
                    Sprinkler {i} (Parcel {i})<br>
                    {'✅ ON' if status == 1 else '<span style="color:#ffffff;">❎ OFF</span>'}
                </div>""", unsafe_allow_html=True)

    st.success("✅ Prediction complete! Sprinklers adjusted accordingly.")

# Footer
st.markdown("""
    <div class="footer">
        © 2025 <a href="https://www.linkedin.com/in/ashwanik48" target="_blank">Ashwani Kumar</a> | Smart Farm AI System 🌾<br>
        Designed with using Streamlit
    </div>
""", unsafe_allow_html=True)
