import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open("zomato_pipeline.pkl","rb"))

st.title("Zomato Restaurant Rating Predictor")

st.write("Enter restaurant details to predict rating")

cost = st.number_input("Average Cost for Two",min_value=0)
votes = st.number_input("Votes",min_value=0)
price_range = st.selectbox("Price Range",[1,2,3,4])
table_booking = st.selectbox("Table Booking",["Yes","No"])
online_delivery = st.selectbox("Online Delivery",["Yes","No"])

if st.button("Predict Rating"):

    features = pd.DataFrame({
        "Average Cost for two":[cost],
        "Price range":[price_range],
        "Votes":[votes],
        "Has Table booking":[table_booking],
        "Has Online delivery":[online_delivery]
    })

    prediction = model.predict(features)

    st.success(f"Predicted Rating: {prediction[0]:.2f} ⭐")