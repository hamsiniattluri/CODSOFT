import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("movies.csv")

vectorizer = CountVectorizer()
genre_matrix = vectorizer.fit_transform(movies["genre"])

similarity = cosine_similarity(genre_matrix)

def recommend():

    movie_name = entry.get().lower()

    indices = movies[movies["title"].str.lower() == movie_name].index

    result_box.delete(1.0, tk.END)

    if len(indices) == 0:
        messagebox.showerror("Error", "Movie not found")
        return

    idx = indices[0]

    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    count = 0

    for movie in scores[1:]:

        movie_index = movie[0]

        result_box.insert(
            tk.END,
            movies.iloc[movie_index]["title"] + "\n"
        )

        count += 1

        if count == 5:
            break

root = tk.Tk()

root.title("Movie Recommendation System")
root.geometry("500x400")

title = tk.Label(
    root,
    text="Movie Recommendation System",
    font=("Arial", 16, "bold")
)

title.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

button = tk.Button(
    root,
    text="Recommend",
    command=recommend
)

button.pack(pady=10)

result_box = tk.Text(root, height=12, width=40)
result_box.pack(pady=10)

root.mainloop()