"""
=========================================
Content-Based Book Recommendation System
File : app.py
Author : Maithily Bhatt
=========================================
"""

from flask import Flask, render_template, request
from recommender import recommend_books

app = Flask(__name__)


# ----------------------------------------
# Home Page
# ----------------------------------------

@app.route("/")
def home():
    return render_template("index.html")


# ----------------------------------------
# Recommendation Page
# ----------------------------------------

@app.route("/recommend", methods=["POST"])
def recommend():

    # Get selected interests from checkboxes
    user_interests = request.form.getlist("interests")

    # Get recommendations
    recommendations = recommend_books(user_interests)

    return render_template(
        "result.html",
        recommendations=recommendations
    )


# ----------------------------------------
# Run Application
# ----------------------------------------

if __name__ == "__main__":
    app.run(debug=True)