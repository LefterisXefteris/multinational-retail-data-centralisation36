import pandas as pd
import numpy as np


class DataCleaning:

    

    def clean_user_data(self, table):
        df = pd.DataFrame(table)
        df = df.drop_duplicates(subset=['email_address','address', 'phone_number', 'user_uuid'])
        return df
        


    def clean_card_data(self, table):
        table['card_number']= table['card_number'].astype(str).apply(lambda x: x.strip('?') if '?' else x)
        table['card_number'] = table['card_number'].str.replace(r'\D', '', regex=True)
        
    
    def called_clean_store_data(self, df):
        df.drop(columns='lat', inplace=True)
        df.dropna(subset = ['staff_numbers'],how='any',inplace= True)
        return df
        
        

    def convert_product_weights(self, products_df):
        pass

        
        




