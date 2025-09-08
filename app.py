import streamlit as st
from codes.stock_utils import *

# Create engine and connect to the database
engine = connect_postgresql()

# Get list of watch stocks
watch_stocs_df = get_list_of_watch_stocks(engine);
st.dataframe(watch_stocs_df)

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
    
    # Timeframe selection
    stock_list = [f"{row['ticker']} - {row['short_name']}" for index, row in watch_stocs_df.iterrows()]
    selected_stock = st.selectbox("Select Ticker", stock_list, index=1)
    
    
st.write(selected_stock)
st.write("Stock ticker: ", selected_stock[:3])



