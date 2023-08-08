import streamlit as st
from pipelines import pipeline3

st.title("Movie Opinion Mining")
st.snow()

def visualize_opinions(movie_name):
    # Your visualization logic here
    pipeline3(movie_name=movie_name)

def display_movies_checkbox():
    pass

def main():

    # Input string from the user
    movie_name = st.text_input("Enter a movie title:")

    if st.button("Visualize"):
        visualize_opinions(movie_name)

if __name__ == "__main__":
    main()