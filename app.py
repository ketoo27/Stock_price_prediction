import streamlit as st
from login import auth, logout
from prediction import predict
from profile import user_profile
from database import connect_db
from news import display_news

# Initialize database connection
connect_db()

# Authentication and navigation
auth()

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Home", "Profile", "Stock Prediction","News"])

# Ensure the user is logged in before showing the pages
if st.session_state['logged_in']:

    if page == "Home":
        st.title("Stock Prediction Web App")
        st.write("""
        Welcome to the Stock Prediction Web App, where you can explore stock trends, view historical data, and predict future stock prices. 
        This guide will help you get the most out of the app:
        """)

        # App usage guide
        st.subheader("How to Use This App")
        st.write("""
        1. **Login and Register:** Use the login and register options to create an account or log in to access the app's features.
        2. **Profile Page:** On the Profile page, you can view your personal information and manage your favorite stocks.
            - Use the **Add to Favorites** button on the Prediction page to save stocks to your profile.
            - In the Profile section, each saved stock has a **Remove** button, allowing you to manage your list.
        3. **Stock Prediction:** Enter a stock ticker (e.g., AAPL for Apple) to view historical stock prices and predict future trends.
            - **Add to Favorites:** You can add stocks to your favorite list while on the prediction page.
            - **Visualization:** The app displays interactive charts to help you analyze stock trends and moving averages.
        """)

        # Additional Information
        st.subheader("Features Overview")
        st.write("""
        - **Historical Data Visualization:** View and analyze historical stock prices and moving averages.
        - **Stock Trend Prediction:** Our machine learning model uses past data to predict future stock trends.
        - **Favorites Management:** Save your preferred stocks and access them easily in your profile.
        """)

        # Tips section
        st.subheader("Tips for Accurate Predictions")
        st.write("""
        - Always verify the stock ticker before inputting it for prediction.
        - Predictions are based on historical data and moving averages; consider these as trends, not guarantees.
        - Use the **Add to Favorites** option to easily access and manage frequently tracked stocks.
        """)
    
    elif page == "Profile":
        user_profile()  # Show user profile and favorite stocks
    
    elif page == "Stock Prediction":
        predict()  # Prediction logic
    
    elif page == "News":
        # Show news based on user's choice
        st.title("Latest Stock News")
        stock_ticker = st.text_input("Enter a stock ticker for specific news")
        display_news(stock_ticker)  # Display news for the specific ticker or general news


else:
    st.title("Welcome to Stock Prediction Web App")
    st.write("Please log in or register to access features.")
