import streamlit as st
import pickle
import pandas as pd
import requests

# Load data and similarity matrix
movies_dict = pickle.load(open('../PyCharmMiscProject/movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('../PyCharmMiscProject/similarity.pkl', 'rb'))

# Mood keywords dictionary
mood_keywords = {
    "Happy": ["comedy", "fun", "adventure", "family", "animation", "romance"],
    "Sad": ["drama", "tragedy", "loss", "emotional", "romantic"],
    "Excited": ["action", "thriller", "crime", "superhero", "fight", "spy"],
    "Scared": ["horror", "mystery", "ghost", "zombie", "dark"],
    "Sci-Fi Lover": ["sci-fi", "space", "alien", "future", "technology"],
}

# Fetch poster from TMDB
def fetch_poster(movie_id):
    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=68bf2d5ecf62356140afda67ffa54f1b"
    )
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# Fetch YouTube trailer link from TMDB
def fetch_trailer(movie_id):
    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key=68bf2d5ecf62356140afda67ffa54f1b"
    )
    data = response.json()
    videos = data.get("results", [])
    for video in videos:
        if video['type'] == 'Trailer' and video['site'] == 'YouTube':
            return f"https://www.youtube.com/watch?v={video['key']}"
    return None

# Recommend by movie title
def recommend_by_title(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(
        list(enumerate(distances)), reverse=True, key=lambda x: x[1]
    )[1:6]

    results = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        title = movies.iloc[i[0]].title
        poster = fetch_poster(movie_id)
        trailer = fetch_trailer(movie_id)
        results.append((title, poster, trailer))
    return results

# Recommend by mood
def recommend_by_mood(mood):
    keywords = mood_keywords[mood]
    matched_movies = movies[movies['tags'].apply(lambda x: any(word in x for word in keywords))]

    if matched_movies.empty:
        return []

    sample_movie = matched_movies.sample(1).iloc[0]
    movie_index = movies[movies['title'] == sample_movie['title']].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(
        list(enumerate(distances)), reverse=True, key=lambda x: x[1]
    )[1:6]

    results = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        title = movies.iloc[i[0]].title
        poster = fetch_poster(movie_id)
        trailer = fetch_trailer(movie_id)
        results.append((title, poster, trailer))
    return results

# Streamlit UI
st.title("Movie Recommender System")

option = st.radio("Search by:", ["Movie Title", "Mood"])

if option == "Movie Title":
    selected_movie = st.selectbox("Choose a movie:", movies['title'].values)
else:
    selected_mood = st.selectbox("Choose a mood:", list(mood_keywords.keys()))

if st.button("Recommend"):
    if option == "Movie Title":
        recommendations = recommend_by_title(selected_movie)
    else:
        recommendations = recommend_by_mood(selected_mood)

    if not recommendations:
        st.error("No recommendations found.")
    else:
        cols = st.columns(5)
        for idx, (title, poster, trailer) in enumerate(recommendations):
            with cols[idx]:
                st.text(title)
                st.image(poster)
                if trailer:
                    st.markdown(f"[Watch Trailer]({trailer})", unsafe_allow_html=True)