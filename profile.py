import streamlit as st
from database import get_favorite_stocks, remove_favorite_stock
from prediction import predict

def user_profile():
    st.title(f"Welcome, {st.session_state['username']}")
    st.write("Here is your profile information and favorite stocks.")
    
    # Display favorite stocks
    st.subheader("Favorite Stocks")
    favorites = get_favorite_stocks(st.session_state['username'])
    
    if not favorites:
        st.info("You have no favorite stocks.")
    else:
        for idx, stock in enumerate(favorites):
            col1, col2 = st.columns([3, 1])  # Split into two columns
            
            # Display the stock symbol as a clickable link
            with col1:
                if st.button(f"View {stock}", key=f"view_{stock}_{idx}"):
                 st.Page="Stock Prediction"
            
            # Add a button to remove the stock
            with col2:
                if st.button(f"Remove {stock}", key=f"remove_{stock}_{idx}"):
                    remove_favorite_stock(st.session_state['username'], stock)
                    st.success(f"Removed {stock} from favorites")
                    st.rerun()  # Refresh the page
