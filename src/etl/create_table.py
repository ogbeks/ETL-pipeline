import os
import psycopg2
import sys
from psycopg2 import sql

from ..utils.database import PostgreSQL_DB


def create_tables(folder):
    """ create tables in the PostgreSQL database"""
    folder_path = f'sql/table_schema/{folder}'
    schema=None
    postgresDB = PostgreSQL_DB()
    if folder =='fact':
        schema = postgresDB.STAGING_SCHEMA
    elif folder =='derived':
        schema =postgresDB.ANALYTICS_SCHEMA
    
    try:
        # create table one by one
        # Get all files in folder
        files = os.listdir(folder_path)

        # Iterate through files
        for file in files:
            if file.endswith(".sql"):
                file_path = os.path.join(folder_path, file)
                with open(file_path, "r") as f:
                    query = f.read()
                query=sql.SQL(query).format(schema_name=sql.Identifier(schema))
                postgresDB.execute_query(query,fetchall=False)
                postgresDB.commit()
            
    except (Exception, psycopg2.DatabaseError) as error:
        print(error, file)
    finally:
        postgresDB.close()
