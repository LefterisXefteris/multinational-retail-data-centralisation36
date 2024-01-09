import yaml
import sqlalchemy
from sqlalchemy import create_engine, text


class DatabaseConnector:


    def read_db_creds(self, file):
        with open(file) as f:
            creds = yaml.safe_load(f)
        return creds


    def init_db_engine(self, creds):


        HOST = creds['RDS_HOST']
        USER = creds['RDS_USER']
        PASSWORD = creds['RDS_PASSWORD']
        DATABASE = creds['RDS_DATABASE']
        PORT = creds['RDS_PORT']
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'

        engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")

        return engine
    
    def list_db_tables(self, engine):
        try:
            with engine.connect() as connection:
                result = connection.execute(text("""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'"""))
                for row in result:
                    print(row)
        except Exception as e:
            print("Failed to fecth tables.", e)


    def upload_to_db(self,df, table_name, engine):
        try:
            df.to_sql(table_name, engine, index=False, if_exists= 'replace')
            print("Table uploaded to Sales Data")
        except Exception as e:
            print('Failed to upload local table to aws:', e)

    
        







    

    



    

