import os
import psycopg2
import sys
from psycopg2 import sql
from psycopg2.extras import execute_values
from ..utils.database import PostgreSQL_DB
import boto3
from botocore import UNSIGNED
from botocore.client import Config
import configparser

# Access the configuration settings
# Create a ConfigParser object and read the configuration file
config = configparser.ConfigParser()
config.read('config/settings.ini')
bucket_name =config.get('AWS', 'BUCKET_NAME')
ID = config.get('database','ID')
s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))

def transform_table():
    """ perform analytics on the PostgreSQL database"""
    folder_path = 'sql/analytics'
    postgresDB = PostgreSQL_DB()
    try:
        # Get all files in folder
        files = os.listdir(folder_path)

        # Iterate through files
        for file in files:
            file_name=file.split('.')[0]
            if file.endswith(".sql"):
                file_path = os.path.join(folder_path, file)
                #Reading the Analytic Query
                with open(file_path, "r") as f:
                    query = f.read()
                query=sql.SQL(query).format(schema_name=sql.Identifier(postgresDB.STAGING_SCHEMA))
                data = postgresDB.execute_query(query,fetchall=True)
                data.to_csv(f"data/analytics/{file_name}.csv")
                #Uploading to the Analytics_export folder in AWS
                #upload_aws_bucket(file_name)
                #Uploading the derived analytics to PostgreSQL Analytics Schema
                columns = data.columns.tolist()
                values = data.values.tolist()
                query = f"INSERT INTO {postgresDB.ANALYTICS_SCHEMA}.{file_name} ({','.join(columns)}) VALUES %s"
                execute_values(postgresDB.cursor, query, values)
                postgresDB.commit()  
            
    except (Exception, psycopg2.DatabaseError) as error:
        print(error, file)
    finally:
        postgresDB.close()

def upload_aws_bucket(file_name):
    """"
    Perform the uploading of the analytics result to AWS Bucket
    """
    file_path = f"data/analytics/{file_name}.csv"
    object_path = f"analytics_export/{ID}/{file_name}.csv"
    s3.upload_file(file_path, bucket_name, object_path)
    print(file_name)
