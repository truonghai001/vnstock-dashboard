from datetime import datetime, timedelta
import pytz

from sqlalchemy import create_engine, text
import streamlit as st


# Read the database secrect from toml
DB_USERNAME = st.secrets["DB_USERNAME"]
DB_PASSWORD = st.secrets["DB_PASSWORD"]
DB_HOSTNAME = st.secrets["DB_HOSTNAME"]
DB_PORTNUMBER = st.secrets["DB_PORTNUMBER"]
DB_NAME = st.secrets["DB_NAME"]


@st.cache_data(ttl=3600) # cache for 1 hour
def connect_postgresql():
    # Create a connection string
    conn_string = f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}:{DB_PORTNUMBER}/{DB_NAME}?sslmode=require"
    
    # Create an engine
    engine = create_engine(conn_string)
    return engine



@st.cache_data(ttl=3600) # cache for 1 hour
def get_stock_history_from_db(engine, ticker: str, start: str, end: str):
    """
    get_stock_history_from_db
    Get the VN Stock history from database
    :param engine: Engine -> PostgreSQL engine
    :param ticker: str
    :param start: str
    :param end: str
    :return: DataFrame
    """
    # SQL query to get stock data from db
    get_stock_query = """
        SELECT 
            ticker,
            trading_datetime as time,
            open_price as open,
            high_price as high,
            low_price as low,
            close_price as close,
            trading_volume as volume
        FROM trading_history
        WHERE ticker = :ticker
        AND trading_date BETWEEN :start AND :end;
    """

    df = None
    try:
        with engine.connect() as connection:
            # Execute the query with proper parameter binding
            df = pd.read_sql_query(
                sql=text(get_stock_query),
                con=connection,
                params={"ticker": ticker, "start": start, "end": end}
            )
            df = df.sort_values('time', ascending=False)

    except Exception as e:
        print(f"Error: {e}")

    return df



@st.cache_data(ttl=3600) # cache for 1 hour
def get_list_of_watch_stocks(engine):
    """
    Get list of watch stocks from db
    """
    # fetch list of watch stocks from db
    select_query = f"""
        SELECT DISTINCT
            ws.ticker,
            vs.organ_short_name AS name
        FROM watch_stock ws
        LEFT JOIN vn_stock vs
        ON ws.ticker = vs.ticker
        WHERE ws.is_active
    """
        
    result_select = list()
    with engine.connect() as connection:
        # Example: SELECT query
        query_select = text(select_query)
        result_select = [f"{row.ticker} - {row.name}" for row in connection.execute(query_select)]
        
    return result_select