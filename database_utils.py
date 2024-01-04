import psycopg2
import sqlalchemy
import yaml 
from sqlalchemy import Engine, create_engine, engine_from_config, text, inspect


class DatabaseConnector:
    
    def read_db_creds(self):
        try:
            with open('db_creds.yaml') as f:
                creds = yaml.safe_load(f)
            return creds
        except:
            print("Failed to read creds")


    def init_db_engine(self):

        creds = self.read_db_creds()
        HOST = creds['RDS_HOST']
        USER = creds['RDS_USER']
        PASSWORD = creds['RDS_PASSWORD']
        DATABASE = creds['RDS_DATABASE']
        PORT = creds['RDS_PORT']
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'

        engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")

        return engine
    
    def list_db_tables(self):
        try:
            engine = self.init_db_engine()
            with engine.connect() as connection:
                result = connection.execute(text("""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'"""))
                for row in result:
                    print(row)
        except Exception as e:
            print("Failed to fecth tables.", e)


    def upload_to_db(self, table):

        try:
            engine = self.init_db_engine()
            table.to_sql(table, engine)
        except Exception as e:
            print("Failed to upload table to databse", e)


            

d = DatabaseConnector()
d.upload_to_db('legacy_users')