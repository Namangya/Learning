"""Visualization reference — customization, subplots, figure/axes API."""

import matplotlib.pyplot as plt
import numpy as np

# --- plot customization ---
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9], color="crimson", linewidth=2, linestyle="--", marker="o")
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_title("Customized Plot")
ax.grid(True, alpha=0.3)

# --- subplots ---
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes[0, 0].plot([1, 2], [1, 2])
axes[0, 1].bar(["a", "b"], [3, 4])
axes[1, 0].hist(np.random.randn(100), bins=20)
axes[1, 1].scatter(np.random.rand(20), np.random.rand(20))
plt.tight_layout()

# --- figure vs axes ---
# fig = entire canvas; ax = individual plot area
fig = plt.figure(figsize=(6, 4))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
ax1.text(0.5, 0.5, "Left", ha="center")
ax2.text(0.5, 0.5, "Right", ha="center")
