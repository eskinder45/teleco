import pandas as pd
from sqlalchemy import create_engine
import os




# Fetch database connection parameters from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")




class userInfoAgregation:
    def __init__(self,query):
        self.query = query
    def agregation_by_user_info(self):

        try:
            # Create a connection string
            connection_string = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
            # Create an SQLAlchemy engine
            engine = create_engine(connection_string)
            # Load data into a pandas DataFrame
            df = pd.read_sql_query(self.query, engine)
            print("query executed successfully!")
            return df
        except Exception as e:
            print(f"An error occurred: {e}")
            return None