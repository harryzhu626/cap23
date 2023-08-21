import streamlit as st
from db.sqlite import sql_query_join, sql_query_entities
from visualize import congregate_data, visualize_for_date

st.title("Reddit Movie Opinion Visualization")

def visualize_opinions(selected_movies):
    for movie_name in selected_movies:
        sql_output = sql_query_join(movie_name=movie_name)
        opinions = congregate_data(sql_output)
        pn_graph = visualize_for_date(movie_name, opinions)
        st.pyplot(pn_graph) 


def main():

    st.write('SELECT MOVIES TO VISUALIZE')
    searchable_movies = sql_query_entities()

    selected_movies = []

    for option in searchable_movies:
        selected = st.checkbox(option[0])
        if selected:
            selected_movies.append(option[0])


    if st.button("Visualize"):
        visualize_opinions(selected_movies=selected_movies)
    

if __name__ == "__main__":
    main()