import streamlit as st
import yfinance as yf
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
from database import add_favorite_stock
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import plotly.graph_objects as go

def predict():
    st.title('Stock Trend Prediction')

    if 'username' not in st.session_state:
        st.warning('Please log in to use the prediction feature.')
        return

    user_input = st.text_input('Enter Stock Ticker', 'NVDA')
    favorite = st.button('Add to Favorites')

    if favorite:
        add_favorite_stock(st.session_state['username'], user_input)
        st.success(f'{user_input} added to favorites')

    df = yf.download(user_input, '2000-01-01')

    st.subheader('Data from 2000-Present')
    st.write(df.describe())

    # Closing price vs Time Chart
    st.subheader("Closing Price vs Time")
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df['Close'], label='Close Price')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.set_title(f'{user_input} Stock Price')
    st.pyplot(fig)

    # Prediction logic here 
    # Closing price vs Time Chart with 50 & 200 Moving Average
    st.subheader("Closing Price vs Time Chart with 50 & 200 Moving Average")
    df['ma50'] = df['Close'].rolling(50).mean()  # Add ma50 as a column
    df['ma200'] = df['Close'].rolling(200).mean()  # Add ma200 as a column
    fig = plt.figure(figsize=(12, 6))
    plt.plot(df['Close'], label='Close Price')
    plt.plot(df['ma50'], 'r', label='50-Day Moving Average')
    plt.plot(df['ma200'], 'g', label='200-Day Moving Average')
    plt.title(f'{user_input} Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    st.pyplot(fig)
    
    # Splitting data into training and testing
    data_training = pd.DataFrame(df['Adj Close'][0:int(len(df) * 0.70)])
    data_testing = pd.DataFrame(df['Adj Close'][int(len(df) * 0.70):])

    scaler = MinMaxScaler(feature_range=(0, 1))
    data_training_array = scaler.fit_transform(data_training)

    model = load_model('keras_model.h5')

    past_100_days = data_training.tail(100)
    final_df = pd.concat([past_100_days, data_testing], ignore_index=True)
    input_data = scaler.fit_transform(final_df)

    x_test = []
    y_test = []

    for i in range(100, input_data.shape[0]):
        x_test.append(input_data[i-100:i])
        y_test.append(input_data[i, 0])

    x_test, y_test = np.array(x_test), np.array(y_test)

    y_predicted = model.predict(x_test)
    scaler = scaler.scale_
    scale_factor = 1 / scaler[0]

    y_predicted = y_predicted * scale_factor
    y_test = y_test * scale_factor

    # Plot predictions vs. originals
    st.subheader('Predictions vs Originals')
    fig = plt.figure(figsize=(12, 6))
    plt.plot(y_test, 'b', label='Original')
    plt.plot(y_predicted, 'r', label='Predicted')
    plt.title('Stock Price Prediction')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    st.pyplot(fig)

    # Extract the most recent prediction (latest day predicted price)
    latest_predicted_price = y_predicted[-1].item()

    # Display the most recent predicted price
    st.subheader(f'Latest Predicted Price for {user_input}')
    st.write(f'The predicted stock price for the latest day is: ${latest_predicted_price:.2f}')
    plot_gauge_indicator(df['ma50'], df['ma200'])
    

def plot_gauge_indicator(ma50, ma200):
    """
    Displays a gauge indicator showing bullish or bearish sentiment.
    :param ma50: Latest 50-day Moving Average
    :param ma200: Latest 200-day Moving Average
    """
    # Determine sentiment: Bullish or Bearish
    if ma50.iloc[-1] > ma200.iloc[-1]:  # Compare the most recent values
        sentiment_score = 75  # Bullish
    else:
        sentiment_score = 25  # Bearish

    # Create the gauge figure
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=sentiment_score,
        number={'suffix': "%"},
        gauge={
            'axis': {'range': [0, 100], 'tickvals': []},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 50], 'color': "red"},  # Bearish zone
                {'range': [50, 100], 'color': "green"}  # Bullish zone
            ],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': sentiment_score
                
            }
        }
    ))

    fig.update_layout(
        title="Stock Sentiment Indicator",
        margin=dict(l=20, r=20, t=40, b=20)
    )

    # Display in Streamlit
    st.plotly_chart(fig, use_container_width=True)








