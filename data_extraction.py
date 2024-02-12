import requests
from urllib import request, response
from PyPDF2 import PdfFileReader
import pandas as pd

import json
import boto3


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


    def retrieve_stores_data_and_save(self, url, header):
        list_of_frames = []
        for i in range(451):
            endpoint = f'{url}{i}'
            print(endpoint)
            response = requests.get(endpoint, headers=header)
            if response.status_code == 200:
                list_of_frames.append(pd.json_normalize(response.json()))
            else:
                print(f"Failed to retrieve data for store {i}. Status Code: {response.status_code}")
        result_df = pd.concat(list_of_frames)
        return result_df
    
    def extract_from_s3(self, address):
        '''Extract CSV using s3 address'''
        s3 = boto3.client('s3')
        bucket, key = address.replace("s3://", "").split("/", 1)
        s3.download_file(bucket, key, key)
        df = pd.read_csv(key)
        return df

    
    








    





    

