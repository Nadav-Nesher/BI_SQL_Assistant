import streamlit as st
from PIL import Image

from helper_funcs import employ_langchain_sql_agent


def create_streamlit_frontend():
    """
    Create the Streamlit frontend for the LangChain SQL BI Assistant.

    This function sets up the Streamlit interface with an input field for
    queries and tabs for displaying results and the Entity-Relationship Diagram (ERD).
    """
    st.title("🦜🔗 LangChain SQL BI Assistant for IMDb")
    user_input = st.text_input("What would you like to know about the IMDB database?")
    tab_titles = ['Result', 'ERD Diagram']
    tabs = st.tabs(tab_titles)

    erd_image = Image.open("imdb_database_ERD.png")
    with tabs[1]:
        st.image(erd_image)

    if user_input:
        llm_result = employ_langchain_sql_agent(user_input=user_input)
        with tabs[0]:
            st.write(llm_result)