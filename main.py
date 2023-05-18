from src.utils.database import PostgreSQL_DB
import src.etl.create_table as ct
import src.etl.load as ld

postgresDB = PostgreSQL_DB()
# postgresDB.execute_query(f"DROP TABLE {postgresDB.STAGING_SCHEMA}.reviews",fetchall=False)
# postgresDB.execute_query(f"DROP TABLE {postgresDB.STAGING_SCHEMA}.orders",fetchall=False)
#postgresDB.execute_query(f"DROP TABLE {postgresDB.STAGING_SCHEMA}.shipments_deliveries",fetchall=False)
#postgresDB.commit()
ct.create_tables()
ld.load_tables()
data=postgresDB.execute_query(f"SELECT count(*) total FROM {postgresDB.STAGING_SCHEMA}.shipments_deliveries",fetchall=True)
# query =f"""SELECT *
# FROM pg_depend
# WHERE objid = '{postgresDB.STAGING_SCHEMA}.orders'::regclass;
# """
# postgresDB.execute_query(query,fetchall=True)

#postgresDB.execute_query(f'GRANT ALL PRIVILEGES ON TABLE reviews TO {postgresDB.USERNAME}',fetchall=False)

data.to_csv("all_schema.csv")
postgresDB.commit()
postgresDB.close()