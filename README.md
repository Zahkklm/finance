# 📊 Stock Dashboard

A simple and interactive **Stock Market Dashboard** built with **Python, Streamlit, Matplotlib, and Yahoo Finance API**.  
It allows users to fetch and visualize stock data from **Borsa İstanbul (BIST)**, NASDAQ, or global markets in just a few clicks.  

---

## 🚀 Features
- 🔎 Search any stock by ticker symbol (e.g., **GARAN.IS**, **AKBNK.IS**, **^XU100**)  
- 📈 Interactive line chart of **Closing Price**  
- 📊 Visualization of **20-day Moving Average**  
- 📑 Descriptive statistics (mean, min, max, std, etc.)  
- 🖥️ Clean dashboard layout with **side-by-side charts**  

---

## 🛠️ Tech Stack
- [Python](https://www.python.org/)  
- [Streamlit](https://streamlit.io/)  
- [yfinance](https://github.com/ranaroussi/yfinance)  
- [Matplotlib](https://matplotlib.org/)  

---

## 📦 Installation

Clone the repository and install dependencies:
```bash
git clone https://github.com/Zahkklm/fiannce.git
cd finance
```

Or install dependencies manually:
```bash
pip install streamlit yfinance matplotlib
```

---

## ▶️ Usage

Run the app:
```bash
streamlit run stock_dashboard.py
```

This will start a local web server at:
👉 [http://localhost:8501](http://localhost:8501)  

---

## 📸 Screenshot

**Dashboard Example (GARAN.IS):**

```
+-------------------------------------------+
| Closing Price      | 20-day Moving Average|
+-------------------------------------------+
|   [small chart]    |     [small chart]    |
+-------------------------------------------+
|               Descriptive Statistics       |
|         (mean, min, max, std, etc.)        |
+-------------------------------------------+
```

---

## 🔮 Future Improvements
- ✅ Compare multiple stocks (e.g., GARAN.IS vs ^XU100)  
- ✅ Add volume charts  
- ✅ Export statistics to CSV/Excel  
- ✅ Deploy on **Streamlit Cloud** for live demo  

---

## 👨‍💻 Author
**Özgür Peynirci**  
📧 [ozgurpeynirci@gmail.com](mailto:ozgurpeynirci@gmail.com)  
🌐 [LinkedIn](https://www.linkedin.com/in/ozgur-peynirci/) · [GitHub](https://github.com/Zahkklm)