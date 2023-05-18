from src.utils.database import PostgreSQL_DB
import src.etl.create_table as ct

postgresDB = PostgreSQL_DB()
ct.create_tables()
postgresDB.execute_query("SELECT * FROM orders ",fetchall=True)
#postgresDB.execute_query(query,fetchall=False)
#data.to_csv("dim_products_schema.csv")
postgresDB.commit()
postgresDB.close()