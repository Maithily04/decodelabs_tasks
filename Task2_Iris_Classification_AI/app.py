"""
=========================================
Iris Flower Classification AI
File : app.py
Author : Maithily Bhatt
=========================================
"""

from flask import Flask, render_template, request
from utils import predict_flower

app = Flask(__name__)


# ----------------------------------------
# Home Page
# ----------------------------------------

@app.route("/")
def home():
    return render_template("index.html")


# ----------------------------------------
# Prediction
# ----------------------------------------

@app.route("/predict", methods=["POST"])
def predict():

    try:
        sepal_length = float(request.form["sepal_length"])
        sepal_width = float(request.form["sepal_width"])
        petal_length = float(request.form["petal_length"])
        petal_width = float(request.form["petal_width"])

        prediction = predict_flower(
            sepal_length,
            sepal_width,
            petal_length,
            petal_width
        )

        return render_template(
            "index.html",
            prediction=prediction
        )

    except Exception as e:

        return render_template(
            "index.html",
            prediction=f"Error: {e}"
        )


# ----------------------------------------
# Run Application
# ----------------------------------------

if __name__ == "__main__":
    app.run(debug=True)