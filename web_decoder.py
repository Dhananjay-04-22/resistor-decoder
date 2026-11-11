import streamlit as st

# Configure the web page layout
st.set_page_config(page_title="Resistor Decoder", layout="centered")

st.title("🔋 4-Band Resistor Decoder")

# The visual guide for the user
st.info("**How to read your physical resistor:**\n"
        "* **Look for the gap:** There is a slightly wider gap between the 3rd and 4th band. Put the isolated band on the right.\n"
        "* **The Gold/Silver rule:** A Gold or Silver band will never be first. If you see one, put that side on the right.")

# Resistor color dictionaries
digit_colors = {"Black": 0, "Brown": 1, "Red": 2, "Orange": 3, "Yellow": 4, 
                "Green": 5, "Blue": 6, "Violet": 7, "Gray": 8, "White": 9}
# Exclude Black for the first band to prevent 0 starting values
first_band_colors = list(digit_colors.keys())[1:] 

multiplier_colors = {"Black": 1, "Brown": 10, "Red": 100, "Orange": 1000, 
                     "Yellow": 10000, "Green": 100000, "Blue": 1000000, 
                     "Gold": 0.1, "Silver": 0.01}

tolerance_colors = {"Brown": "±1%", "Red": "±2%", "Green": "±0.5%", 
                    "Blue": "±0.25%", "Violet": "±0.1%", "Gold": "±5%", "Silver": "±10%"}

# Create 4 columns for a clean UI layout
col1, col2, col3, col4 = st.columns(4)

with col1:
    band1 = st.selectbox("Band 1 (1st Digit)", first_band_colors)
with col2:
    band2 = st.selectbox("Band 2 (2nd Digit)", list(digit_colors.keys()))
with col3:
    band3 = st.selectbox("Band 3 (Multiplier)", list(multiplier_colors.keys()))
with col4:
    band4 = st.selectbox("Band 4 (Tolerance)", list(tolerance_colors.keys()))

# Calculation logic
base_value = (digit_colors[band1] * 10) + digit_colors[band2]
multiplier = multiplier_colors[band3]
resistance = base_value * multiplier

# Format the output to look clean (e.g., turning 1000 into 1k)
if resistance >= 1000000:
    formatted_resistance = f"{resistance / 1000000:g} MΩ"
elif resistance >= 1000:
    formatted_resistance = f"{resistance / 1000:g} kΩ"
else:
    formatted_resistance = f"{resistance:g} Ω"

st.divider()

# Display the final result in large text
st.metric(label="Calculated Resistance", value=f"{formatted_resistance} {tolerance_colors[band4]}")