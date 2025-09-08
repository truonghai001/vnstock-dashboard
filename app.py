import streamlit as st
from codes.stock_utils import *
from datetime import datetime, timedelta
import pytz
from codes.constants import *



# Create engine and connect to the database
engine = connect_postgresql()

# Get list of watch stocks
watch_stocs_df = get_list_of_watch_stocks(engine)


# set up page configuration
st.set_page_config(
    page_title="VN Stock Dashboard",
    page_icon="📈",
    layout="wide"
)

st.write("#📈 VN Stock Dashboard")

today = datetime.now(pytz.timezone('Asia/Ho_Chi_Minh'))
sb_end_date = (today + timedelta(days=-1)).strftime('%Y-%m-%d')
sb_start_date = (today + timedelta(days=DAY_INTERVAL)).strftime('%Y-%m-%d')
min_date = (today + timedelta(days=BACK_NUMBER_OF_YEARS*365)).strftime('%Y-%m-%d')

# sidebar setting
with st.sidebar:
    st.sidebar.header("Stock Settings")
    
    # ticker selection
    stock_list = [f"{row['ticker']} - {row['short_name']}" for index, row in watch_stocs_df.iterrows()]
    selected_stock = st.selectbox("Select Ticker", stock_list, index=1)
    
    # Start & End date select box
    select_dates = st.date_input(
        "Select Start & End Date: ",
        (sb_start_date, sb_end_date),
        min_date, 
        today.strftime('%Y-%m-%d'),
        format="YYYY-MM-DD"
    )
    
    # Refresh button
    refresh = st.button("Refresh")
    
    

if refresh:
    st.write("Select Dates: ", select_dates)
    st.write("Stock ticker: ", selected_stock)

    # Get parameters from sidebar
    ticker = selected_stock[:3]
    start_date = select_dates[0].strftime('%Y-%m-%d')
    end_date = select_dates[1].strftime('%Y-%m-%d')

    st.write("Start Date: ", start_date)
    st.write("End Date: ", end_date)

    stock_df = get_stock_history_from_db(engine, ticker, start_date, end_date)
    st.dataframe(stock_df)

