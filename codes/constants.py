import streamlit as st

# Read the database secrect from toml
DB_USERNAME = st.secrets["DB_USERNAME"]
DB_PASSWORD = st.secrets["DB_PASSWORD"]
DB_HOSTNAME = st.secrets["DB_HOSTNAME"]
DB_PORTNUMBER = st.secrets["DB_PORTNUMBER"]
DB_NAME = st.secrets["DB_NAME"]

# Read day interval
DAY_INTERVAL = st.secrets["DAY_INTERVAL"]
BACK_NUMBER_OF_YEARS = st.secrets["BACK_NUMBER_OF_YEARS"]