"""ML starter — train/test split, preprocessing, Pipeline, fit, score."""

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, classification_report

# Load sample data
X, y = load_iris(return_X_y=True)

# --- train_test_split ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# --- preprocessing + Pipeline ---
pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("clf", LogisticRegression(max_iter=200)),
])

# --- fit ---
pipe.fit(X_train, y_train)

# --- score / evaluation ---
train_score = pipe.score(X_train, y_train)
test_score = pipe.score(X_test, y_test)
print(f"Train accuracy: {train_score:.4f}")
print(f"Test accuracy:  {test_score:.4f}")

y_pred = pipe.predict(X_test)
print(classification_report(y_test, y_pred))
