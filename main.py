from data_cleaning import DataCleaning
from data_extraction import DataExtractor
from database_utils import DatabaseConnector
import pandas as pd


if __name__ == '__main__':
    
    de = DataExtractor()
    du = DatabaseConnector()
    dc = DataCleaning()


    creds = du.read_db_creds('db_creds.yaml')
    engine = du.init_db_engine(creds)
    list_tables = du.list_db_tables(engine)
    user_data = de.read_rds_table('legacy_users', engine)
    clean_user_data = dc.clean_user_data(user_data)
    print(clean_user_data.head())
  

    
   # Testing local databse
    
    creds_local = du.read_db_creds('local_db_cred.yaml')
    local_engine = du.init_db_engine(creds_local)
    local_tables = du.list_db_tables(local_engine)
    #print(local_tables)"""

    #Uploads the cleaned DF to local_databse

    du.upload_to_db(clean_user_data,'dim_users', local_engine)

  #Retrive data from pdf to Pandas DF
    card = du.retrieve_pdf_data('files/card_details.pdf', 'files/output.csv')
    
    clean_card = dc.clean_card_data(card)
    print(clean_card)
    du.upload_to_db(clean_card, 'dim_card',local_engine )


    #list stores from X api
    
    header = {
        'x-api-key':'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'
    }
    
    url = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores'
    print("nUmber of stores: " , de.list_number_of_stores(header, url))

    full_url = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number}'
    api_key = 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'


    response_in_list = de.retrieve_stores_data_and_save('https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/', header)
    print(response_in_list.head(10))
  
    du.upload_to_db(response_in_list, 'dim_store_details', local_engine)
    
    print(de.extract_from_s3('s3://data-handling-public/products.csv').head())