import requests
import streamlit as st

API_KEY = "991U1U6CMIEPST10"

def fetch_news(stock_symbol=None):
    if stock_symbol:
        url = f"https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={stock_symbol}&apikey={API_KEY}"
    else:
        url = f"https://www.alphavantage.co/query?function=NEWS_SENTIMENT&apikey={API_KEY}"
    
    response = requests.get(url)
    data = response.json()
    
    if 'feed' in data:
        return data['feed']
    else:
        st.warning("No news data available or exceeded API call limit.")
        return []

def display_news(stock_symbol=None):
    st.header("Latest Stock News")
    if stock_symbol:
        st.subheader(f"News for {stock_symbol}")
    else:
        st.subheader("General Stock News")

    news_items = fetch_news(stock_symbol)
    if news_items:
        for article in news_items:
            st.markdown(f"### {article['title']}")
            st.markdown(f"*{article['time_published']}*")
            st.markdown(f"{article['summary']}")
            st.markdown(f"[Read more]({article['url']})")
            st.write("---")

