import streamlit as st
import time

# ✅ Set page configuration FIRST
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

# ✅ Custom CSS for Black & Red Theme + Smooth Styling
st.markdown(
    """
    <style>
    body, .stApp {
        background-color: black !important;
        color: red !important;
    }
    .stTextInput input, .stNumberInput input, .stSelectbox select, .stButton>button {
        background-color: black !important;
        color: red !important;
        border: 2px solid red !important;
    }
    .stButton>button {
        border-radius: 10px !important;
        font-size: 16px !important;
        font-weight: bold !important;
    }
    .result-box {
        padding: 15px;
        background-color: rgba(255, 0, 0, 0.3);
        border: 2px solid red;
        border-radius: 10px;
        text-align: center;
        font-size: 20px;
        animation: fadeIn 1s ease-in-out;
    }
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ✅ Title
st.title(" Unit Converter")

# ✅ Conversion Functions
def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        "meters": {"feet": 3.28084, "meters": 1, "kilometers": 0.001, "miles": 0.000621371},
        "feet": {"meters": 0.3048, "feet": 1, "kilometers": 0.0003048, "miles": 0.000189394},
        "kilometers": {"meters": 1000, "feet": 3280.84, "kilometers": 1, "miles": 0.621371},
        "miles": {"meters": 1609.34, "feet": 5280, "kilometers": 1.60934, "miles": 1}
    }
    return value * conversion_factors[from_unit][to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    return value

def convert_weight(value, from_unit, to_unit):
    conversion_factors = {
        "kilograms": {"kilograms": 1, "grams": 1000, "pounds": 2.20462},
        "grams": {"kilograms": 0.001, "grams": 1, "pounds": 0.00220462},
        "pounds": {"kilograms": 0.453592, "grams": 453.592, "pounds": 1}
    }
    return value * conversion_factors[from_unit][to_unit]

def convert_time(value, from_unit, to_unit):
    conversion_factors = {
        "seconds": {"seconds": 1, "minutes": 1/60, "hours": 1/3600},
        "minutes": {"seconds": 60, "minutes": 1, "hours": 1/60},
        "hours": {"seconds": 3600, "minutes": 60, "hours": 1}
    }
    return value * conversion_factors[from_unit][to_unit]

def convert_speed(value, from_unit, to_unit):
    conversion_factors = {
        "m/s": {"m/s": 1, "km/h": 3.6, "mph": 2.23694},
        "km/h": {"m/s": 0.277778, "km/h": 1, "mph": 0.621371},
        "mph": {"m/s": 0.44704, "km/h": 1.60934, "mph": 1}
    }
    return value * conversion_factors[from_unit][to_unit]

def convert_area(value, from_unit, to_unit):
    conversion_factors = {
        "sq meters": {"sq meters": 1, "sq km": 0.000001, "sq miles": 0.0000003861},
        "sq km": {"sq meters": 1000000, "sq km": 1, "sq miles": 0.3861},
        "sq miles": {"sq meters": 2589988.11, "sq km": 2.589988, "sq miles": 1}
    }
    return value * conversion_factors[from_unit][to_unit]

# ✅ Sidebar for Category Selection
category = st.sidebar.selectbox("Select Conversion Category", ["Length", "Temperature", "Weight", "Time", "Speed", "Area"])

# ✅ User Input
value = st.number_input("Enter Value", min_value=0.0, max_value=100000.0, step=0.1)

# ✅ Select input and output units dynamically
if category == "Length":
    from_unit = st.selectbox("From", ["meters", "feet", "kilometers", "miles"])
    to_unit = st.selectbox("To", ["meters", "feet", "kilometers", "miles"])
    result = convert_length(value, from_unit, to_unit)

elif category == "Temperature":
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit"])
    to_unit = st.selectbox("To", ["Celsius", "Fahrenheit"])
    result = convert_temperature(value, from_unit, to_unit)

elif category == "Weight":
    from_unit = st.selectbox("From", ["kilograms", "grams", "pounds"])
    to_unit = st.selectbox("To", ["kilograms", "grams", "pounds"])
    result = convert_weight(value, from_unit, to_unit)

elif category == "Time":
    from_unit = st.selectbox("From", ["seconds", "minutes", "hours"])
    to_unit = st.selectbox("To", ["seconds", "minutes", "hours"])
    result = convert_time(value, from_unit, to_unit)

elif category == "Speed":
    from_unit = st.selectbox("From", ["m/s", "km/h", "mph"])
    to_unit = st.selectbox("To", ["m/s", "km/h", "mph"])
    result = convert_speed(value, from_unit, to_unit)

elif category == "Area":
    from_unit = st.selectbox("From", ["sq meters", "sq km", "sq miles"])
    to_unit = st.selectbox("To", ["sq meters", "sq km", "sq miles"])
    result = convert_area(value, from_unit, to_unit)

# ✅ Display Result with Animation
if value > 0:
    st.markdown(
        f"""
        <div class="result-box">
            <h2>{value} {from_unit} = {result:.4f} {to_unit}</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ✅ Reset Button to Rerun the App
if st.button("Reset"):
    st.rerun()
