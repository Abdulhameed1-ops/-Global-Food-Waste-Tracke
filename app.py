import streamlit as st
import pandas as pd
import numpy as np
from streamlit_lottie import st_lottie
import requests

# Lottie Animation JSON file for background animation (Get one from LottieFiles)
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Main App Function
def main():
    # Set page config for custom width/height and theme
    st.set_page_config(page_title="Global Food Waste Tracker", page_icon="🍞", layout="wide")
    
    # Load background animation
    lottie_bg = load_lottie_url("https://assets7.lottiefiles.com/packages/lf20_buoqslhs.json")
    
    # Header section with background animation
    st_lottie(lottie_bg, speed=1, width=900, height=400, key="background")

    st.title("🌍 Global Food Waste Tracker")
    st.subheader("Track, Measure, and Reduce Your Food Waste!")

    st.write("""
    Food waste is one of the largest global problems today. With this app, you can track your food waste, get insights, and find ways to reduce it.
    """)
    
    # Create a sidebar for navigation and settings
    st.sidebar.title("Navigation")
    menu = ["Home", "Log Waste", "Waste Analytics", "Waste Reduction Tips", "Donation Network"]
    choice = st.sidebar.selectbox("Select Option", menu)

    if choice == "Home":
        home_page()
    elif choice == "Log Waste":
        log_waste()
    elif choice == "Waste Analytics":
        waste_analytics()
    elif choice == "Waste Reduction Tips":
        reduction_tips()
    elif choice == "Donation Network":
        donation_network()

# Home page with introductory info
def home_page():
    st.header("Welcome to the Global Food Waste Tracker!")
    st.write("This app is dedicated to reducing global food waste by helping you track and manage your food waste.")
    st.write("Let's get started on reducing food waste today!")

# Log Waste Page
def log_waste():
    st.header("Log Your Food Waste")
    st.write("Enter the food items you have wasted today.")

    food_item = st.text_input("Food Item")
    category = st.selectbox("Category", ["Fruits & Veggies", "Dairy", "Meat", "Grains", "Other"])
    amount = st.number_input("Amount Wasted (in grams)", min_value=0)

    if st.button("Log Waste"):
        if food_item and amount > 0:
            st.success(f"Logged {amount}g of {food_item} in the {category} category.")
        else:
            st.error("Please enter valid information.")
    
# Waste Analytics Page
def waste_analytics():
    st.header("Your Food Waste Analytics")
    st.write("See how much food you're wasting over time.")
    
    # Dummy data for visualization (This can be dynamic in the future with user data)
    data = {
        "Category": ["Fruits & Veggies", "Dairy", "Meat", "Grains", "Other"],
        "Amount (g)": [200, 50, 150, 30, 20],
    }
    
    df = pd.DataFrame(data)
    st.bar_chart(df.set_index("Category"))

# Waste Reduction Tips Page
def reduction_tips():
    st.header("Waste Reduction Tips")
    st.write("Here are some easy tips to reduce food waste:")
    
    tips = [
        "Plan meals ahead of time to avoid excess food buying.",
        "Freeze leftovers or soon-to-expire food to extend shelf life.",
        "Use food scraps to make stock or compost.",
        "Store fruits and veggies properly to extend their shelf life."
    ]
    
    for tip in tips:
        st.write(f"- {tip}")

# Donation Network Page
def donation_network():
    st.header("Donate Unused Food to Local Charities")
    st.write("Help your community by donating unused food to local food banks.")
    st.write("Find the nearest donation centers in your area.")

    # Dummy data for charity locations (you can integrate with APIs for actual locations)
    donation_centers = ["Food Bank A", "Food Bank B", "Community Shelter C"]
    st.write("Nearby Donation Centers:")
    for center in donation_centers:
        st.write(f"- {center}")
        
if __name__ == "__main__":
    main()
