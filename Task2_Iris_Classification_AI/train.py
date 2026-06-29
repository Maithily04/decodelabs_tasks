"""
=========================================
Iris Flower Classification AI
File : train.py
Author : Maithily Bhatt
=========================================
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
import joblib
import os


# ----------------------------------------
# Load Dataset
# ----------------------------------------

iris = load_iris()

X = iris.data
y = iris.target


# ----------------------------------------
# Train-Test Split
# ----------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ----------------------------------------
# Train Model
# ----------------------------------------

model = KNeighborsClassifier(n_neighbors=3)

model.fit(X_train, y_train)


# ----------------------------------------
# Test Model
# ----------------------------------------

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average="weighted")


# ----------------------------------------
# Print Results
# ----------------------------------------

print("=" * 45)
print("Iris Flower Classification Model")
print("=" * 45)

print(f"\nAccuracy : {accuracy * 100:.2f}%")

print("\nConfusion Matrix:")
print(conf_matrix)

print(f"\nF1 Score : {f1:.4f}")


# ----------------------------------------
# Save Model
# ----------------------------------------

os.makedirs("model", exist_ok=True)

joblib.dump(model, "model/iris_model.pkl")

print("\nModel saved successfully!")
print("Location : model/iris_model.pkl")