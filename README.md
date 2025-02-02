Project Overview
The Stock Prediction Web App is an interactive web-based platform that enables users to analyze stock trends, predict future stock prices, and manage their favorite stocks. Built using Streamlit, TensorFlow, and Yahoo Finance API, the app provides an intuitive interface for stock market enthusiasts to make informed decisions based on historical data and machine learning predictions.

Key Features
🔹 User Authentication & Profile Management
Users can register and log in securely.
A personalized profile page displays the user’s favorite stocks.
Users can add or remove stocks from their favorites.
📈 Stock Data Visualization
Fetches real-time stock data from Yahoo Finance.
Displays historical price trends using Matplotlib and Plotly.
Shows moving averages (50-day & 200-day) for trend analysis.
🔮 Stock Price Prediction using LSTM Model
Uses a trained LSTM (Long Short-Term Memory) model to predict future stock prices.
Compares predicted vs. actual stock prices in graphical format.
Displays the latest predicted stock price for informed decision-making.
📊 Technical Indicators & Sentiment Analysis
Implements 50-day & 200-day moving averages for trend identification.
Features a gauge indicator that visually represents stock sentiment:
Bullish (Green Side) → MA50 is above MA200.
Bearish (Red Side) → MA50 is below MA200.
📰 Stock News Integration (Planned Feature)
Retrieves latest news articles for selected stocks using Alpha Vantage API.
Allows users to filter news by specific stock symbols.
Technology Stack
Frontend: Streamlit (Python)
Backend: Flask (for authentication & database management)
Machine Learning: TensorFlow/Keras (LSTM Model)
Database: SQLite (to store user favorites)
Data Source: Yahoo Finance API
Visualization: Matplotlib, Plotly
How It Works
User logs in → Accesses their profile.
Enters a stock ticker → Fetches historical stock data.
Sees price trends & moving averages → Visualizes stock movements.
Predicts stock prices → LSTM model forecasts the next price.
Analyzes sentiment → Gauge indicator shows bullish/bearish trends.
Adds stocks to favorites → Easily track and revisit predictions.
