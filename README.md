# 📉 Gap Down Recovery Trading Strategy – Python Backtest (5-Year Data)

![IBM words previous week](https://github.com/Nikhil-Jagtap619/Nifty-500-Prototype/blob/main/Screenshot%202025-06-19%20162401.png)

This project simulates a simple **price-action-based trading strategy** on Indian stocks (e.g., TCS) using **5 years of historical stock data**.

It identifies buying opportunities based on a 3-step pattern and tracks the performance of each trade using Python, with output exported to Excel.

---

## 📌 Project Objective

To test a **gap down + recovery breakout** strategy on Indian stocks and evaluate the trade performance over the last 5 years using actual historical data.

---

## 🧠 Strategy Logic (Simplified)

1. A stock **gaps down by 2% or more** compared to the previous day's close.
2. It **recovers** to the previous close (on the same day or later).
3. It then **breaks out** by rising another 2% or more.
4. **Buy Trigger**: Enter trade at this 2% breakout price.
5. **Exit Conditions**:
   - 🎯 **Target**: Exit at +10% profit
   - 🛑 **Stop Loss**: Exit at -5% loss
   - ⏱️ **Max Hold**: Exit after 60 calendar days if no target or stop hit


