"""
=========================================
Content-Based Book Recommendation System
File : recommender.py
Author : Maithily Bhatt
=========================================
"""

from data import books


def recommend_books(user_interests):
    """
    Recommend books based on user interests.

    Parameters:
        user_interests (list): List of selected interests.

    Returns:
        list: Recommended book titles.
    """

    recommendations = []

    # Check every book
    for book in books:

        score = 0

        # Compare book tags with user interests
        for tag in book["tags"]:

            if tag in user_interests:
                score += 1

        # Store books with at least one matching tag
        if score > 0:
            recommendations.append({
                "title": book["title"],
                "score": score
            })

    # Sort by highest score
    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    # Return only book titles
    return [book["title"] for book in recommendations]