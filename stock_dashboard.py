import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import datetime as dt

st.set_page_config(page_title="Stock Dashboard", layout="wide")

# Sidebar for user input
st.sidebar.header("Stock Dashboard")

# Default values
default_ticker = "GARAN.IS"
today = dt.date.today()
one_year_ago = today - dt.timedelta(days=365)

ticker = st.sidebar.text_input("Enter Stock Symbol (e.g., GARAN.IS, AKBNK.IS, ^XU100)", default_ticker)
start_date = st.sidebar.date_input("Start Date", one_year_ago)
end_date = st.sidebar.date_input("End Date", today)

if ticker:
    try:
        data = yf.download(ticker, start=start_date, end=end_date)

        if not data.empty:
            st.title(f"📊 Stock Dashboard for {ticker}")

            # Create two columns for charts
            col1, col2 = st.columns(2)

            # Closing Price
            with col1:
                st.subheader("Closing Price")
                fig, ax = plt.subplots(figsize=(3,1.5))
                ax.plot(data.index, data["Close"], label="Close Price", color="blue")
                ax.set_xlabel("Date", fontsize=6)
                ax.set_ylabel("Price", fontsize=6)
                ax.tick_params(axis='both', labelsize=6)
                ax.legend(fontsize=6)
                st.pyplot(fig, clear_figure=True)

            # Moving Average
            with col2:
                st.subheader("20-day MA")
                data["MA20"] = data["Close"].rolling(20).mean()
                fig, ax = plt.subplots(figsize=(3,1.5))
                ax.plot(data.index, data["Close"], label="Close Price", alpha=0.7)
                ax.plot(data.index, data["MA20"], label="20-day MA", color="red")
                ax.tick_params(axis='both', labelsize=6)
                ax.legend(fontsize=6)
                st.pyplot(fig, clear_figure=True)

            # Statistics (full width)
            st.subheader("Statistics")
            st.dataframe(data.describe().style.format("{:.2f}"))

        else:
            st.error("⚠️ No data found. Try another ticker like AKBNK.IS or ^XU100")
    except Exception as e:
        st.error(f"Error fetching data: {e}")
