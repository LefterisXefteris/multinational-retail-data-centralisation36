import requests
from urllib import request, response
from PyPDF2 import PdfFileReader
import pandas as pd


class DataExtractor:


    def read_rds_table(self, table_name, engine):
        try:
            df = pd.read_sql_table(table_name, engine)
            return df
        except Exception as e:
            print("Failed to read the tables", e)

    
    def list_number_of_stores(self, header, url):
        response = requests.get(url, headers = header)
        json_re = response.json()
        return json_re['number_stores']

    def retrieve_stores_data(self, url, header):
            
        list_of_frames = []
        for i in range(452):
            response = requests.get(f'{url}{i}',headers=self.header)
            list_of_frames.append(pd.json_normalize(response.json()))
        return pd.concat(list_of_frames)









    





    

