from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

movies = pd.read_csv("movies.csv")

vectorizer = CountVectorizer()
genre_matrix = vectorizer.fit_transform(movies["genre"])

similarity = cosine_similarity(genre_matrix)

def recommend_movies(movie_name):
    movie_name = movie_name.lower()

    indices = movies[movies["title"].str.lower() == movie_name].index

    if len(indices) == 0:
        return []

    idx = indices[0]

    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    recommendations = []

    for movie in scores[1:6]:
        movie_index = movie[0]

        recommendations.append(
            movies.iloc[movie_index]["title"]
        )

    return recommendations

@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = []

    if request.method == "POST":
        movie_name = request.form["movie"]
        recommendations = recommend_movies(movie_name)

    return render_template(
        "index.html",
        recommendations=recommendations
    )

if __name__ == "__main__":
    app.run(debug=True)