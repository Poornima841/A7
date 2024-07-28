import streamlit as st
import pandas as pd

# Load the calorie data
def load_data():
    data = pd.read_csv('calories.csv')
    return data

data = load_data()

st.title("Calorie Checker")

st.write("Welcome to the Calorie Checker app! Select a food item to see its calorie content.")

# Sidebar for user input
st.sidebar.header("Select Food Item")
food_item = st.sidebar.selectbox("Food", data["Food"])

# Display calorie content
calories = data.loc[data["Food"] == food_item, "Calories"].values[0]
st.write(f"The calorie content of {food_item} is {calories} calories.")

# Show the data table
st.write("Here is the full list of food items and their calorie content:")
st.write(data)
