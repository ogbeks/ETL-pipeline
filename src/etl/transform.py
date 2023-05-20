import os
import psycopg2
import sys
from psycopg2 import sql

from ..utils.database import PostgreSQL_DB


def transform_table():
    """ create tables in the PostgreSQL database"""
    folder_path = 'sql/analytics'
    postgresDB = PostgreSQL_DB()
    try:
        # create table one by one
        # Get all files in folder
        files = os.listdir(folder_path)

        # Iterate through files
        for file in files:
            print(file)
            if file.endswith(".sql"):
                file_path = os.path.join(folder_path, file)
                with open(file_path, "r") as f:
                    query = f.read()
                query=sql.SQL(query).format(schema_name=sql.Identifier(postgresDB.STAGING_SCHEMA))
                data = postgresDB.execute_query(query,fetchall=True)
                data.to_csv(f"data/analytics/{file.split('.')[0]}.csv")
                print(file)
            
    except (Exception, psycopg2.DatabaseError) as error:
        print(error, file)
    finally:
        postgresDB.close()


# # if __name__ == '__main__':
#     create_tables()