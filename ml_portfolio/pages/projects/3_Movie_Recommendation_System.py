import streamlit as st
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import difflib

# Set page config
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title("🎬 Movie Recommendation System")

# Load data
@st.cache_data
def load_data():
    movies = pd.read_csv("data/movies.csv")
    ratings = pd.read_csv("data/ratings.csv")
    return movies, ratings

movies, ratings = load_data()

# Preprocessing
@st.cache_data
def preprocess(movies, ratings):
    # Merge ratings with movie titles
    data = pd.merge(ratings, movies, on='movieId')

    # Calculate mean rating & count per movie
    movie_stats = data.groupby('title').agg(avg_rating=('rating', 'mean'), rating_count=('rating', 'count')).reset_index()

    # Join stats with movies
    movies_merged = pd.merge(movies, movie_stats, on='title')

    # Fill missing genres
    movies_merged['genres'] = movies_merged['genres'].fillna('')

    # Create genre matrix using CountVectorizer (limit to top 5000 movies to avoid memory crash)
    top_movies = movies_merged.sort_values(by='rating_count', ascending=False).head(5000)
    count_vec = CountVectorizer(tokenizer=lambda x: x.split('|'))
    genre_matrix = count_vec.fit_transform(top_movies['genres'])

    similarity = cosine_similarity(genre_matrix)

    return top_movies.reset_index(drop=True), similarity

top_movies, similarity = preprocess(movies, ratings)

# Movie title input with fuzzy matching
user_input = st.text_input("🔍 Enter a movie title", placeholder="e.g., The Dark Knight Rises")

if user_input:
    movie_titles = top_movies['title'].tolist()
    matches = difflib.get_close_matches(user_input, movie_titles, n=5, cutoff=0.6)

    if matches:
        selected_title = matches[0]
        st.success(f"✅ Showing recommendations for: **{selected_title}**")

        movie_idx = top_movies[top_movies['title'] == selected_title].index[0]
        sim_scores = list(enumerate(similarity[movie_idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        st.subheader("📽️ Top 5 Similar Movies:")
        for i, (idx, score) in enumerate(sim_scores[1:6], start=1):
            movie = top_movies.iloc[idx]
            st.markdown(f"""
            **{i}. {movie['title']}**
            - 🎯 Genres: `{movie['genres']}`
            - ⭐ Average Rating: `{movie['avg_rating']:.2f}` ({int(movie['rating_count'])} ratings)
            """)

    else:
        st.error("🚫 Movie not found.")
        st.markdown("🔎 Try checking the spelling or entering a more complete title.")





