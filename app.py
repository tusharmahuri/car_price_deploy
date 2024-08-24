import streamlit as st
import pandas as pd
import pickle

# Load the saved model
loaded_model = pickle.load(open('car_price_prediction_model_streamlit.pkl', 'rb'))

# Sample data (replace this with your actual dataset)
data = pd.read_csv("cleaned car.csv")

# Streamlit app
st.title('Car Price Prediction')

# Select company
selected_company = st.selectbox('Select Company', data['company'].unique())

# Filter names based on selected company
filtered_names = data[data['company'] == selected_company]['name'].unique()

# Select car name
selected_name = st.selectbox('Select Car Name', filtered_names)

# Input year
year = st.number_input('Enter Year', min_value=2005, max_value=2024, value=2019)

# Input kms driven
kms_driven = st.number_input('Enter Kilometers Driven', min_value=0, max_value=500000, value=60000)

# Select fuel type
fuel_type = st.selectbox('Select Fuel Type', data['fuel_type'].unique())

# Predict button
if st.button('Predict Price'):
    # Create DataFrame for the new data
    new_data = pd.DataFrame({
        'name': [selected_name],
        'company': [selected_company],
        'year': [year],
        'kms_driven': [kms_driven],
        'fuel_type': [fuel_type]
    })

    # Make prediction
    predicted_price = loaded_model.predict(new_data)

    # Display the prediction
    st.write(f"Predicted Price: ₹{predicted_price[0]:,.2f}")
