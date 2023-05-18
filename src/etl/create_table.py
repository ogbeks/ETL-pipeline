import os
import psycopg2
import sys

from utils.database import PostgreSQL_DB


def create_tables():
    """ create tables in the PostgreSQL database"""
    folder_path = 'sql/table_schema'
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
                postgresDB.execute_query(query,fetchall=False)
                postgresDB.commit()
            
    except (Exception, psycopg2.DatabaseError) as error:
        print(error, file)
    finally:
        postgresDB.close()


# # if __name__ == '__main__':
#     create_tables()