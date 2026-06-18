import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("movies.csv")

vectorizer = CountVectorizer()
genre_matrix = vectorizer.fit_transform(movies["genre"])

similarity = cosine_similarity(genre_matrix)

def recommend(movie_name):
    movie_name = movie_name.lower()

    indices = movies[movies["title"].str.lower() == movie_name].index

    if len(indices) == 0:
        print("Movie not found!")
        return

    idx = indices[0]

    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print("\nRecommended Movies:\n")

    count = 0

    for i in scores[1:]:
        movie_index = i[0]

        print(movies.iloc[movie_index]["title"])

        count += 1

        if count == 5:
            break

movie = input("Enter Movie Name: ")

recommend(movie)