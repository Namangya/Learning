"""Visualization starter — line, bar, histogram, scatter with matplotlib and seaborn."""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# --- Line plot ---
x = np.linspace(0, 10, 100)
plt.figure(figsize=(8, 4))
plt.plot(x, np.sin(x), label="sin(x)")
plt.title("Line Plot")
plt.legend()
plt.savefig("line_plot.png")
plt.close()

# --- Bar chart ---
categories = ["A", "B", "C"]
values = [23, 45, 56]
plt.bar(categories, values, color="steelblue")
plt.title("Bar Chart")
plt.savefig("bar_chart.png")
plt.close()

# --- Histogram ---
data = np.random.randn(1000)
plt.hist(data, bins=30, edgecolor="black", alpha=0.7)
plt.title("Histogram")
plt.savefig("histogram.png")
plt.close()

# --- Scatter plot ---
sns.scatterplot(x=np.random.rand(50), y=np.random.rand(50), hue=np.random.randint(0, 3, 50))
plt.title("Scatter Plot (Seaborn)")
plt.savefig("scatter_plot.png")
plt.close()
