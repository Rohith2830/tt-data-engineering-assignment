import pandas as pd
from pathlib import Path

INPUT_FILE = "stocks.csv"        # input CSV
OUTPUT_DIR = "output"            # output folder
Path(OUTPUT_DIR).mkdir(exist_ok=True)

df = pd.read_csv(INPUT_FILE)
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(["ticker", "date"])

monthly = (
    df.set_index("date")
      .groupby("ticker")
      .resample("ME")   # Month End (future-safe)
      .agg(
          open=("open", "first"),     # first trading day
          high=("high", "max"),       # monthly high
          low=("low", "min"),         # monthly low
          close=("close", "last"),    # last trading day
          volume=("volume", "sum")
      )
      .reset_index()
)


monthly = monthly.sort_values(["ticker", "date"])

monthly["SMA_10"] = monthly.groupby("ticker")["close"].transform(
    lambda x: x.rolling(10).mean()
)
monthly["SMA_20"] = monthly.groupby("ticker")["close"].transform(
    lambda x: x.rolling(20).mean()
)
monthly["EMA_10"] = monthly.groupby("ticker")["close"].transform(
    lambda x: x.ewm(span=10, adjust=False).mean()
)
monthly["EMA_20"] = monthly.groupby("ticker")["close"].transform(
    lambda x: x.ewm(span=20, adjust=False).mean()
)


for ticker, group in monthly.groupby("ticker"):
    group.to_csv(f"{OUTPUT_DIR}/result_{ticker}.csv", index=False)

print("✅ All 10 monthly output files generated successfully")
