# Data Engineering Intern Hiring Assignment

## Objective
The objective of this assignment is to transform daily stock price data into
monthly aggregated data and compute technical indicators using Python and Pandas.

---

## Input Data
- Single CSV file containing 2 years of daily stock prices
- Columns:
  date, volume, open, high, low, close, adjclose, ticker
- Tickers:
  AAPL, AMD, AMZN, AVGO, CSCO, MSFT, NFLX, PEP, TMUS, TSLA

---

## Monthly Aggregation Logic
Daily data is resampled to monthly frequency using the following rules:
- Open: Price on the first trading day of the month
- Close: Price on the last trading day of the month
- High: Maximum price during the month
- Low: Minimum price during the month
- Volume: Sum of daily volumes in the month

---

## Technical Indicators
Technical indicators are calculated using monthly closing prices:
- SMA 10: 10-month Simple Moving Average
- SMA 20: 20-month Simple Moving Average
- EMA 10: 10-month Exponential Moving Average
- EMA 20: 20-month Exponential Moving Average

EMA is calculated using Pandas `ewm(span=N, adjust=False)` which follows the
standard EMA formula.

---

## Output
- 10 separate CSV files are generated (one per ticker)
- Each file contains exactly 24 rows (24 months)
- File naming format: result_<TICKER>.csv

---

## Assumptions
1. The dataset contains exactly 2 years (24 months) of data for each ticker.
2. The input data includes only valid trading days.
3. Technical indicators are calculated only after monthly aggregation.
4. Initial SMA values are NaN until enough periods are available.
5. The solution uses only Python and Pandas (no third-party TA libraries).

---

## How to Run
```bash
pip install pandas
python src/process_stocks.py

