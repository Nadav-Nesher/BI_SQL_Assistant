import os
from dotenv import load_dotenv
from langchain.utilities import SQLDatabase
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import create_sql_agent
from langchain.agents.agent_types import AgentType
from langchain.llms import OpenAI


# Retrieve OpenAI API key from environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Retrieve DB connection variables from environment variables
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

pg_uri = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"


def employ_langchain_sql_agent(user_input: str,
                               model_name: str = 'gpt-3.5-turbo-1106',
                               temperature: float = 0) -> str:
    """
    Employ LangChain's SQL agent to process and respond to a user's question/query.
    Upon receiving the user's input, it will process it, generate an SQL query and get back
    the LLM's analysed output in natural language.

    This function creates a connection to the SQL database, initializes the
    LangChain SQL agent with the provided model, and executes the user's query
    using the agent.

    Parameters:
    - user_input (str): The user's question in natural language.
    - model_name (str, optional): The name of the LLM model to be used. Defaults to 'gpt-3.5-turbo-1106'.
    - temperature (float, optional): The creativity level the LLM should use. Defaults to 0.

    Returns:
    - str: The result from the LangChain SQL agent (the LLM's natural language response).
    """

    db = SQLDatabase.from_uri(pg_uri)
    llm = OpenAI(temperature=temperature, api_key=OPENAI_API_KEY, model_name=model_name)
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    agent_executor = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        handle_parsing_errors=True
    )
    llm_result = agent_executor.run(user_input)

    return llm_result