import sqlalchemy
import yaml 
from sqlalchemy import create_engine, engine_from_config, text

class DatabaseConnector:
    

    def read_db_creds(self):
        with open("credentials.yaml", "r") as f:
            credentials = yaml.safe_load(f)
        return credentials
    
    def init_db_engine(self):
        creds = self.read_db_creds()
        con_str = f"postgresql://{creds['RDS_USER']}:{creds['RDS_PASSWORD']}@{creds['RDS_HOST']}:{creds['RDS_PORT']}/{creds['RDS_DATABASE']}"
        engine = sqlalchemy.create_engine(con_str)
        return engine






