import steam_recommender
import streamlit as st

PAGES = {
    "Steam Game Recommender": steam_recommender
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
