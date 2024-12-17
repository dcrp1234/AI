import streamlit as st
import pickle
import pandas as pd
import requests

def add_custom_css():
    st.markdown(
        """
               <style>
               /* General App Background and Text Color */
               .stApp {
                   background-color: black;
                   color: white;
               }

                 /* Titles and Headers */
                .css-1d391kg {  /* class name used by Streamlit for titles */
                    color: white;
                }
                .css-10trblm {  /* class name used by Streamlit for subheaders */
                    color: white;
                }

               /* Buttons */
                .movie-button {
                background-color: transparent;
                border: none;
                color: white;
                padding: 0;
                cursor: pointer;
                font-size: 16px;
                text-align: left;
               }
     
               .stButton>button {
                   background-color: #4CAF50;
                   color: white;
                   border: none;
                   border-radius: 5px;
                   padding: 10px 24px;
                   font-size: 16px;
               }
               .stButton>button:hover {
                   background-color: #45a049;
               }
               

               /* Selectbox */
               .stSelectbox > div > div {
                   background-color: black;
                   color: white;
               }

               /* Input Box */
               .stTextInput > div > div > input {
                   background-color: black;
                   color: white;
               }

               /* Other text elements */
               .stMarkdown, .stText {
                   color: white;
               }
               </style>
               """,
        unsafe_allow_html=True
    )

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=ed5aad40ca2db18de8e84029bd1efb07&language=en-US'.format(movie_id))
    data = response.json()
    s = "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    return s

def fetch_info(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=ed5aad40ca2db18de8e84029bd1efb07&language=en-US'.format(movie_id))
    data = response.json()
    s = data['overview']
    return s

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1: 11]

    recommended_movies = []
    recommended_movies_poster = []
    recommended_movies_overview = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        #fetch poster from API
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies_overview.append(fetch_info(movie_id))
    return recommended_movies, recommended_movies_poster, recommended_movies_overview


movies_dict = pickle.load(open('movie_dict.pkl', 'rb' ))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('Movie Recommender System')

add_custom_css()

selected_movie_name = st.selectbox(
'Select a movie:',
movies['title'].values
)

if st.button('Recommend'):
    names, posters, overview = recommend(selected_movie_name)

    cols = st.columns(5)

    # Add content to each column
    for i, col in enumerate(cols):
        with col:
            st.image(posters[i])
            st.write(names[i])

  # button = []
   #  for i, name in enumerate(names):
    #    button.append(st.button(names[i]))
                #st.write(overview[i])
            # Display the movie poster



