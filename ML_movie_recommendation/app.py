import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response= requests.get("https://api.themoviedb.org/3/movie/{}?api_key=2e6ffacd0054f31b37192432b3018716&language=en-US".format(movie_id))
    data= response.json()
    print(data)
    return "https://image.tmdb.org/t/p/original/" + data["poster_path"]
def recommend(movie):
    movie_index= movies[movies['title'] == movie].index[0]
    distances= similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x: x[1])[1:6]

    recommended_movies=[]
    recommended_movies_poster= []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        #fethcing the posters
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
        # print(i[0])

    return recommended_movies, recommended_movies_poster

similarity= pickle.load(open('similarity.pkl','rb'))
movies_dict= pickle.load(open('movied.pkl','rb'))
movies =  pd.DataFrame(movies_dict)
st.title('Movie Recommeneder System')
selected_movie_name= st.selectbox(
    'what movie recommendation would you like?',
    movies['title'].values
)

if st.button('Recommend'):
    recommendations, posters= recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommendations[0])
        st.image(posters[0])
    with col2:
        st.text(recommendations[1])
        st.image(posters[1])
    with col3:
        st.text(recommendations[2])
        st.image(posters[2])
    with col4:
        st.text(recommendations[3])
        st.image(posters[3])
    with col5:
        st.text(recommendations[4])
        st.image(posters[4])
