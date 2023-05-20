import psycopg2
import pandas as pd
import configparser

# Create a ConfigParser object and read the configuration file
config = configparser.ConfigParser()
config.read('config/settings.ini')

class PostgreSQL_DB():
  def __init__(self) -> None:
    self.USERNAME = config.get("database", "USERNAME")
    self.PASSWORD = config.get("database", "PASSWORD")
    self.HOST = config.get("database", "HOST")
    self.PORT = int(config.get("database", "PORT"))
    self.DB_NAME = config.get("database", "DB_NAME")
    self.STAGING_SCHEMA = config.get("database", "STAGING_SCHEMA")
    self.ANALYTICS_SCHEMA = config.get("database", "ANALYTICS_SCHEMA")
    # PostgreSQL database connection string
    self.DB_STRING = f"postgresql+psycopg2://{self.USERNAME}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DB_NAME}"

    self.conn = psycopg2.connect(
                      user=self.USERNAME,
                      password=self.PASSWORD,
                      host=self.HOST,
                      port=self.PORT,
                      database=self.DB_NAME)
    self.cursor = self.conn.cursor()
    self.cursor.execute(f"SET search_path TO {self.STAGING_SCHEMA};")


  def execute_query(self, query, fetchall=False):
    try:
      self.cursor.execute(query)
    except (Exception, psycopg2.DatabaseError) as error:
      print(error)
    finally:
      if fetchall:
        results = self.cursor.fetchall()
        column_names = [desc[0] for desc in self.cursor.description]
        df = pd.DataFrame(results, columns=column_names)
        print(df)
        return df
        
  def commit(self):
    try:
      self.conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
      print(error)
  
  def close(self):
    if self.cursor:
      self.cursor.close()
    if self.conn:
      self.conn.close()
