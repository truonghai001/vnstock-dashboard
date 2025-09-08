import streamlit as st
from codes.stock_utils import *

# set up page configuration
st.set_page_config(
    page_title="VN Stock Dashboard",
    page_icon="📈",
    layout="wide"
)

st.write("#📈 VN Stock Dashboard")

# sidebar setting
with st.sidebar:
    st.sidebar.header("Stock Settings")
    
    # show list of tickers

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)

st.write("DB username:", st.secrets["DB_USERNAME"])

# Create engine and connect to the database
engine = connect_postgresql()
