from datetime import datetime, timedelta
import pytz

from sqlalchemy import create_engine, text
import psycopg2
import streamlit as st


# Read the database secrect from toml
DB_USERNAME = st.secrets["DB_USERNAME"]
DB_PASSWORD = st.secrets["DB_PASSWORD"]
DB_HOSTNAME = st.secrets["DB_HOSTNAME"]
DB_PORTNUMBER = st.secrets["DB_PORTNUMBER"]
DB_NAME = st.secrets["DB_NAME"]

st.write("DB username:", st.secrets["db_username"])

def connect_postgresql():
    # Create a connection string
    conn_string = f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}:{DB_PORTNUMBER}/{DB_NAME}?sslmode=require"
    
    # Create an engine
    engine = create_engine(conn_string)
    return engine