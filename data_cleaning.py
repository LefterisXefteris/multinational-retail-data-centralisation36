import pandas as pd
import numpy as np


class DataCleaning:

    

    def clean_user_data(self, df):
        clean_user_data = df.drop_duplicates(subset=['email_address', 'address', 'phone_number', 'user_uuid'], keep='last').reset_index(drop=True)
        clean_user_data = df[df["country_code"].str.len() <= 2]
        return clean_user_data







