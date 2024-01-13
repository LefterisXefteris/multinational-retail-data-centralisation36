from PyPDF2 import PdfFileReader
import pandas as pd


class DataExtractor:


    def read_rds_table(self, table_name, engine):
        try:
            df = pd.read_sql_table(table_name, engine)
            return df
        except Exception as e:
            print("Failed to read the tables", e)

    


    


