import pandas as pd
import numpy as np 
from data_extraction import DataExtractor
from database_utils import DatabaseConnector
from datetime import datetime
import re



class DataCleaning:

    def __init__(self, dataframe=DataExtractor()):
        self.dataframe = dataframe
     

    def clean_user_data(self, user_data):
        df = self.dataframe.read_rds_table(user_data)
        clean_user_data = df.drop_duplicates(subset= ['email_address', 'address', 'phone_number', 'user_uuid'], keep = 'last').reset_index(drop = True)
        return clean_user_data
    



c = DataCleaning()
print(c.clean_user_data('legacy_users'))
