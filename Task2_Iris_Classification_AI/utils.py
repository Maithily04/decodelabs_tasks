"""
=========================================
Iris Flower Classification AI
File : utils.py
Author : Maithily Bhatt
=========================================
"""

import joblib
import numpy as np


# ----------------------------------------
# Load Trained Model
# ----------------------------------------

model = joblib.load("model/iris_model.pkl")


# ----------------------------------------
# Flower Names
# ----------------------------------------

flower_names = [
    "Iris Setosa 🌸",
    "Iris Versicolor 🌼",
    "Iris Virginica 🌺"
]


# ----------------------------------------
# Prediction Function
# ----------------------------------------

def predict_flower(sepal_length, sepal_width, petal_length, petal_width):
    """
    Predict the Iris flower species.
    """

    features = np.array([
        [
            sepal_length,
            sepal_width,
            petal_length,
            petal_width
        ]
    ])

    prediction = model.predict(features)[0]

    return flower_names[prediction]