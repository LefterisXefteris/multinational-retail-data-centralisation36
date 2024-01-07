
import pandas as pd

from database_utils import DatabaseConnector

class DataExtractor:

    def __init__(self, instance = DatabaseConnector()):
        self.instance = instance
        


    def read_rds_table(self, table_name):
        try:
            engine = self.instance.init_db_engine()
            df = pd.read_sql_table(table_name, engine)
            return df
        except Exception as e:
            print("Failed to read the tables", e)



if __name__ == '__main__':
    
    de = DataExtractor()
    user_data = de.read_rds_table('legacy_users')
    print(user_data)
   


    
    
