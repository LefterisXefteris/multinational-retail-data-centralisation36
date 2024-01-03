from sqlalchemy import create_engine, engine_from_config, text
import tabula
from database_utils import DatabaseConnector
import pandas as pd
import tabula
from tabula import read_pdf
from database_utils import read_db_creds, init_db_engine
from data_cleaning import data
import PyPDF2


class DataExtractor:
    

    def read_rds_table(self):
        pass
        
