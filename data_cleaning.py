import pandas as pd
import numpy as np


class DataCleaning:

    

    def clean_user_data(self, table):
        clean_user_data = table.drop_duplicates(subset=['email_address', 'address', 'phone_number', 'user_uuid'], keep='last').reset_index(drop=True)
        clean_user_data = table.loc[table['country_code'].str.len() <= 2]

        return clean_user_data


    def clean_card_data(self, table):

        table['card_number']= table['card_number'].astype(str).apply(lambda x: x.strip('?') if '?' else x)
        
        return table 
       


        



        
        




