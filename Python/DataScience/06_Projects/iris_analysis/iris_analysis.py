"""Iris analysis — EDA + classification scaffold."""

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# --- Load data ---
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = iris.target_names[iris.target]

# --- EDA ---
print(df.describe())
print(df.groupby("species").mean())

# --- Classification ---
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42
)
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)
print(classification_report(y_test, clf.predict(X_test)))
