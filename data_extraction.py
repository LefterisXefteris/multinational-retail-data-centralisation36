from sqlalchemy import engine_from_config, text
import tabula
from database_utils import read_db_creds, init_db_engine
import pandas as pd
from tabula import read_pdf


class DataExtractor:
    

    def list_databe_tables(self):
        try: 
            with engine_from_config.connect() as connection:
                query = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
                tables = pd.read_sql_query(query, connection)
                print("Tables in the database:")
                for table in tables['table_name']:
                    print(table)
        except Exception as e:
            print("Failed to fetch tables:", e)



    def read_rds_table(self, table_name):
        table_name = self.list_databe_tables()
        return table_name
    
    def retrieve_pdf_data(self):
        the_link = "https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf"
        link_to_pdf = tabula.read_pdf(the_link)
        return link_to_pdf
