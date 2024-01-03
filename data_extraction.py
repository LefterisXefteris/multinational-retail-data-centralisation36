from sqlalchemy import Engine, create_engine, engine_from_config, text
from database_utils import DatabaseConnector
import pandas as pd
import tabula
from tabula import read_pdf



class DataExtractor():

    def __init__(self, instance = DatabaseConnector()):
        self.instance = instance

    def read_rds_table(self):
        try:
            engine = self.instance.init_db_engine()
            with engine.connect() as connection:
                result = connection.execute(text("SELECT * FROM legacy_users"))
                df = pd.read_sql_table('legacy_users', engine)
                print(df.head(10))
        except Exception as e:
            print("FAILED", e)
        
        
        


e = DataExtractor()
e.read_rds_table()