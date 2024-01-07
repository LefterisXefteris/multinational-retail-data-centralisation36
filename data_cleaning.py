import pandas as pd



class DataCleaning:

    def __init__(self, user_table):
        self.user_table = user_table

    def clean_user_data(self, user_data, df):
        clean_user_data = df.drop_duplicates(subset=['email_address', 'address', 'phone_number', 'user_uuid'], keep='last').reset_index(drop=True)
        return clean_user_data



if __name__ =='__name__':
    pass

    

