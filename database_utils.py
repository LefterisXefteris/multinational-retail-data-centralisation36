import yaml 

class DatabaseConnector:
    
    def read_db_creds():
        with open("credentials.yaml", "r") as f:
            credentials = yaml.safe_load(f)
        return credentials