"""Pandas reference — indexing, merge, reshape, time series."""

import pandas as pd

# --- indexing ---
df = pd.DataFrame({"x": [1, 2, 3]}, index=["a", "b", "c"])
print(df.loc["a"])       # label-based
print(df.iloc[0])        # position-based

# --- merge ---
left = pd.DataFrame({"key": ["A", "B"], "val_l": [1, 2]})
right = pd.DataFrame({"key": ["A", "C"], "val_r": [3, 4]})
print(pd.merge(left, right, on="key", how="inner"))

# --- reshape (pivot) ---
tall = pd.DataFrame({"date": ["2024-01", "2024-01", "2024-02"],
                     "product": ["A", "B", "A"], "sales": [10, 20, 15]})
print(tall.pivot(index="date", columns="product", values="sales"))

# --- time series ---
ts = pd.date_range("2024-01-01", periods=5, freq="D")
series = pd.Series(range(5), index=ts)
print(series.resample("2D").sum())
