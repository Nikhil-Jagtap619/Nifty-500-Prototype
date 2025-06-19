#importing necessary libraries
import streamlit as st
import pandas as pd
import yfinance as yf

nifty_list = pd.read_csv("ind_nifty500list.csv")


def get_analysis(data,stock, trades):
   for i in range(2, len(data)):
    prev_close = data.iloc[i - 1]["Close"][0]
    today_open = data.iloc[i]["Open"][0]

    if today_open <= prev_close * 0.98:
        for j in range(i, min(i + 60, len(data))):
            high = data.iloc[j]["High"][0]
            if high >= prev_close:
                if high >= prev_close * 1.02:
                    entry_price = round(prev_close * 1.02, 2)
                    entry_date = data.index[j]

                    for k in range(j, min(j + 60, len(data))):
                        high_k = data.iloc[k]["High"][0]
                        low_k = data.iloc[k]["Low"][0]
                        close_k = data.iloc[k]["Close"][0]
                        exit_date = data.index[k]

                        if high_k >= entry_price * 1.10:
                            exit_price = round(entry_price * 1.10, 2)
                            outcome = "Target Hit"
                            break
                        elif low_k <= entry_price * 0.95:
                            exit_price = round(entry_price * 0.95, 2)
                            outcome = "Stop Loss"
                            break
                        elif k == j + 59:
                            exit_price = round(close_k, 2)
                            outcome = "Max Hold"
                            break

                    trades.append({
                        "Stock": stock,
                        "Entry Date": entry_date.date(),
                        "Entry Price": entry_price,
                        "Exit Date": exit_date.date(),
                        "Exit Price": exit_price,
                        "P&L (%)": round((exit_price - entry_price) / entry_price * 100, 2),
                        "Days Held": (exit_date - entry_date).days,
                        "Outcome": outcome
                    })
                    break



def main():
    st.sidebar.title("All Nifty 500 List")
    st.sidebar.dataframe(nifty_list[["Symbol","Company Name","Industry"]], height=620)
    st.title("Gap Down Recovery Trading Strategy Nifty 50")
    st.write("This project simulates a simple price action based trading strategy on Indian stocks (e.g., TCS) using 5 years of historical stock data.")
    user_stk = st.text_input("Paste your company symbol to fetch data (only NSE)").upper() + ".NS"
    trades = []
    user_period = st.text_input("What time duration you looking for? Enter just a number (only in years)") + "y"
    user_interval = st.text_input("What interval would you like? Enter just a number (only in days)") + "d"
    stock = user_stk
   

    if st.button("Analyze"):
         data = yf.download(stock, period=user_period, interval=user_interval)
         data["Prev_Close"] = data["Close"].shift(1)
         data = data.dropna().copy()
         get_analysis(data, stock, trades)
         df = pd.DataFrame(trades)
         st.dataframe(df)





    st.write("## Thank you for Visiting \nPrototype by Nikhil J")
    st.markdown("<h1 style='text-align: right; color: #d7e3fc; font-size: small;'><a href='https://github.com/Nikhil-Jagtap619/Nifty-500-Prototype'>Visit my Github to know more</a></h1>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()