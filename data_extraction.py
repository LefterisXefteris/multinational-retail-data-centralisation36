from PyPDF2 import PdfFileReader
import pandas as pd
from tabula import read_pdf

class DataExtractor:


    def read_rds_table(self, table_name, engine):
        try:
            df = pd.read_sql_table(table_name, engine)
            return df
        except Exception as e:
            print("Failed to read the tables", e)

    def retrieve_pdf_data(self, link):
        df_temp = read_pdf(link, pages='all', multiple_tables=True)
        return df_temp





