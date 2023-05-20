import os
import psycopg2
import sys
import pandas as pd
from ..utils.database import PostgreSQL_DB
from sqlalchemy import create_engine
from psycopg2.extras import execute_values

postgresDB = PostgreSQL_DB()
print(postgresDB.DB_STRING)
engine = create_engine(postgresDB.DB_STRING)

def load_tables():
  folder_path = 'data/raw'
  try:
    # Get all files in folder
    files = os.listdir(folder_path)
    # Iterate through files
    for file in files:
      file_name=file.split('.')[0]
      if file_name=='reviews' or file_name=='orders':
        continue
      if file.endswith(".csv"):
        file_path = os.path.join(folder_path, file)
        data=pd.read_csv(file_path) 
        print(data.info())
        print(data.head())
        if file_name=='orders':
          data.rename(columns={'total_price':'amount'},inplace=True)
        columns = data.columns.tolist()
        values = data.values.tolist()
        query = f"INSERT INTO {postgresDB.STAGING_SCHEMA}.{file_name} ({','.join(columns)}) VALUES %s"
        execute_values(postgresDB.cursor, query, values)
        postgresDB.commit()
            
  except (Exception) as error:
    print(error, file)
  finally:
    postgresDB.close()



