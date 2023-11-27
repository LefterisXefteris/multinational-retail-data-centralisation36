from sqlalchemy import engine_from_config, text
from database_utils import read_db_creds, init_db_engine
import pandas as pd


class DataExtractor:
    

    def list_databe_tables(self):
        try: 
            with engine_from_config.connect() as connection:
                query = text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
                result = connection.execute(query)
                tables = result.fetchall()
                print("Tables in the database:")
                for table in tables:
                    print(table[0])
        except Exception as e:
            print("Failed to fetch tables:", e)



    def read_rds_table(self, table_name):
        con_engine = init_db_engine()  
        table_data = pd.read_sql(f'SELECT * FROM {table_name}', con_engine)
        return table_data