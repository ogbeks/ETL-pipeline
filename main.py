from src.utils.database import PostgreSQL_DB
import src.etl.create_table as ct
import src.etl.load as ld
import src.etl.transform as tf
import src.etl.extract as et

postgresDB = PostgreSQL_DB()
def main():
  et.extract()
  ct.create_tables('fact')
  ct.create_tables('derived')
  ld.load_tables()
  tf.transform_table()
  
main()