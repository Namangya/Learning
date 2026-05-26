"""Statistics reference — scipy.stats API, p-values, confidence intervals."""

from scipy import stats
import numpy as np

# --- scipy.stats API overview ---
# Continuous: norm, t, chi2, f, expon, uniform
# Discrete: binom, poisson
# Tests: ttest_1samp, ttest_ind, chi2_contingency, mannwhitneyu

# --- p-values ---
# p-value = probability of observing data at least as extreme, assuming H0 is true
# Typically reject H0 if p < 0.05
data = np.random.randn(30)
_, p = stats.ttest_1samp(data, popmean=0)
print(f"p-value (H0: mean=0): {p:.4f}")

# --- confidence intervals ---
# 95% CI for the mean using t-distribution
n = len(data)
mean = np.mean(data)
se = stats.sem(data)
ci = stats.t.interval(0.95, df=n - 1, loc=mean, scale=se)
print(f"95% CI for mean: ({ci[0]:.4f}, {ci[1]:.4f})")
