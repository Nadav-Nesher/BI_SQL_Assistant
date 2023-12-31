from streamlit_frontend import create_streamlit_frontend

def flow():
    """
    Executes the main workflow of the application.

    Initialize the Streamlit frontend for the BI Assistant.
    Calls the function to create and display the Streamlit frontend.
    """
    create_streamlit_frontend()


if __name__ == '__main__':
    """
    Main execution point of the script. Calls the flow function.
    """
    flow()