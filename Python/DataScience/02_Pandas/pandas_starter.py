"""Pandas starter — DataFrames, I/O, filtering, groupby, missing values."""

import pandas as pd
import numpy as np

# --- DataFrame creation ---
data = {"name": ["Alice", "Bob", "Carol"], "age": [25, 30, 28], "city": ["NYC", "LA", "Chicago"]}
df = pd.DataFrame(data)
print(df.head())

# --- read_csv ---
# df = pd.read_csv("data.csv")  # uncomment when you have a CSV file
# print(df.info())

# --- Filtering ---
adults = df[df["age"] >= 28]
print(adults)

# --- groupby aggregation ---
sales = pd.DataFrame({"region": ["East", "West", "East", "West"], "revenue": [100, 200, 150, 250]})
by_region = sales.groupby("region")["revenue"].sum()
print(by_region)

# --- fillna / missing values ---
df_with_nan = pd.DataFrame({"a": [1, np.nan, 3], "b": [4, 5, np.nan]})
filled = df_with_nan.fillna(0)
print(filled)
