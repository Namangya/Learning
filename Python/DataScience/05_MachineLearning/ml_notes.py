"""ML reference — model types, cross-validation, metrics."""

from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, f1_score, roc_auc_score
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

# --- model types ---
# Classification: LogisticRegression, RandomForest, SVM, KNN
# Regression: LinearRegression, Ridge, RandomForestRegressor
# Clustering: KMeans, DBSCAN

# --- cross-validation ---
clf = RandomForestClassifier(n_estimators=100, random_state=42)
scores = cross_val_score(clf, X, y, cv=5, scoring="accuracy")
print(f"CV accuracy: {scores.mean():.4f} (+/- {scores.std():.4f})")

# --- metrics ---
# Classification: accuracy, precision, recall, F1, ROC-AUC
# Regression: MSE, RMSE, MAE, R-squared
clf.fit(X, y)
y_pred = clf.predict(X)
print("Confusion matrix:\n", confusion_matrix(y, y_pred))
print("F1 (macro):", f1_score(y, y_pred, average="macro"))
