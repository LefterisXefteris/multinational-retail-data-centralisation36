import pandas as pd



class DataCleaning:

    def clean_user_data(self, df):
        clean_user_data = df.drop_duplicates(subset=['email_address', 'address', 'phone_number', 'user_uuid'], keep='last').reset_index(drop=True)
        
        return clean_user_data





    

