Movie Recommender System

This is a Movie Recommender System that suggests movies based on a given movie title or user mood. The system uses Natural Language Processing (NLP) and Cosine Similarity for recommending movies. It also includes a web-based interface built using Streamlit.

 Features:

- Movie recommendations based on movie titles.
- Mood-based movie recommendations (e.g., happy, sad, excited).
- Uses NLP techniques for text processing and Cosine Similarity for calculating similarity.
- Interactive user interface built with Streamlit.
- Movie posters and trailers fetched from TMDB API.

 
 Technologies Used:
 
- Python
- Streamlit (for the web app interface)
- Scikit-learn (for NLP and Cosine Similarity)
- Pandas & Numpy (for data manipulation)
- Requests (for fetching movie posters and trailers)
- TMDB API (for movie poster and trailer data)

Installation:

To run the project locally, follow these steps:

1. Clone the repository:

   bash
   git clone https://github.com/your-username/movie-recommender-system.git
   

2. Navigate to the project folder:

   bash
   cd movie-recommender-system
   

3. Create a virtual environment (optional but recommended):

   bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   

4. Install required dependencies:

   bash
   pip install -r requirements.txt
   

5. Download the necessary pickle files (movies_dict.pkl and similarity.pkl) if they are not present in the repository. These files can be created by running the Python script to generate them (or you can use the pre-existing ones).

6. Run the Streamlit app:

   bash
   streamlit run app.py
   

- How It Works

 Data Preparation

- The project starts by importing two datasets:

  - tmdb_5000_movies.csv: Contains movie information such as title, overview, genres, etc.
  - tmdb_5000_credits.csv: Contains movie credits like cast and crew.

- After merging the datasets, preprocessing is applied to handle missing values, remove duplicates, and format columns like genres, keywords, cast, and crew into a clean list.

- Additional data cleaning includes tokenizing the 'overview', and applying stemming techniques to reduce words to their base forms.

-Recommendation Engine

- The recommendation engine works by calculating the Cosine Similarity between movies based on a combination of their genres, keywords, cast, crew, and overview tags.
- The engine recommends movies based on either:

  1. Movie Title: Users input a movie title, and the system returns similar movies.
  2. Mood: Users select a mood (like Happy, Sad, Excited), and the system suggests movies that fit that mood based on related keywords.

- Streamlit App

-The Streamlit app allows users to interact with the movie recommender by entering a movie title or selecting a mood.
-The app fetches movie posters and YouTube trailers from the *TMDB API* and displays them alongside the recommended movie titles.

