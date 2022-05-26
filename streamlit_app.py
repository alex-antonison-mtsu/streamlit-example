from collections import namedtuple
import pandas as pd
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

"""
# Welcome to Streamlit!

This is a sample Streamlit App that includes how to work with a database
"""


with st.echo(code_location="below"):

    user = st.secrets["username"]
    pwd = st.secrets["password"]
    host = st.secrets["host"]
    engine = create_engine(f"postgresql+psycopg2://{user}:{pwd}@{host}/dear_database")

    @st.experimental_memo(ttl=600)
    def get_data(_engine, table_name):

        query = """
        select * 
        from dear_database.public.demographic 
        """

        with engine.connect() as conn:
            queried_df = pd.read_sql(query, con=conn)

        return queried_df

    df = get_data(engine, "demographics")

    st.write(df.head())
