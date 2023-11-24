import yaml 
from sqlalchemy import create_engine

class DatabaseConnector:
    
    def read_db_creds():
        with open("credentials.yaml", "r") as f:
            credentials = yaml.safe_load(f)
        return credentials
    
    def init_db_engine():
        creds = read_db_creds()

        conn_str = f"{creds['driver']}://{creds['user']}:{creds['password']}@{creds['host']}:{creds['port']}/{creds['database']}"

        engine = sqlalchemy.create_engine(conn_str)
        return engine


















ss = DatabaseConnector()
sa = ss.read_db_creds
print(sa)