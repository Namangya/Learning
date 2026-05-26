"""Statistics starter — descriptive stats, distributions, hypothesis testing, correlation."""

from scipy import stats
import numpy as np

# --- Descriptive statistics ---
sample = np.array([2.1, 3.4, 5.6, 7.8, 4.2, 6.1, 3.9])
print("Mean:", np.mean(sample))
print("Std:", np.std(sample, ddof=1))
print("scipy describe:", stats.describe(sample))

# --- Probability distributions ---
# Normal distribution PDF and random samples
x = np.linspace(-4, 4, 100)
pdf = stats.norm.pdf(x, loc=0, scale=1)
samples = stats.norm.rvs(loc=0, scale=1, size=1000, random_state=42)

# --- Hypothesis testing ---
# One-sample t-test: is the mean significantly different from 0?
t_stat, p_value = stats.ttest_1samp(sample, popmean=5.0)
print(f"t-statistic: {t_stat:.4f}, p-value: {p_value:.4f}")

# --- Correlation ---
x_var = np.array([1, 2, 3, 4, 5])
y_var = np.array([2, 4, 5, 4, 5])
r, p = stats.pearsonr(x_var, y_var)
print(f"Pearson r: {r:.4f}, p-value: {p:.4f}")
