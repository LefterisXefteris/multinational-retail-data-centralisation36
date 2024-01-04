from sqlalchemy import Engine, create_engine, engine_from_config, text
from database_utils import DatabaseConnector
import pandas as pd
import tabula
from tabula import read_pdf



class DataExtractor():

    def __init__(self, instance = DatabaseConnector()):
        self.instance = instance

    def read_rds_table(self, table_name):
        engine = self.instance.init_db_engine()
        df = pd.read_sql_table(table_name, engine)
        return df
    


        
""""        
e = DataExtractor()
print(e.read_rds_table('legacy_users'))"""