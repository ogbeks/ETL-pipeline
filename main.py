from src.utils.database import PostgreSQL_DB
import src.etl.create_table as ct
import src.etl.load as ld
import src.etl.transform as tf

postgresDB = PostgreSQL_DB()
# postgresDB.execute_query(f"DROP TABLE {postgresDB.STAGING_SCHEMA}.reviews",fetchall=False)
# postgresDB.execute_query(f"DROP TABLE {postgresDB.STAGING_SCHEMA}.orders",fetchall=False)
#postgresDB.execute_query(f"DROP TABLE {postgresDB.STAGING_SCHEMA}.shipments_deliveries",fetchall=False)
#postgresDB.commit()
# ct.create_tables()
# ld.load_tables()
tf.transform_table()
#data=postgresDB.execute_query(f"SELECT count(*) total FROM {postgresDB.STAGING_SCHEMA}.shipments_deliveries",fetchall=True)
#data=postgresDB.execute_query(f"SELECT o.*, cdd.* FROM {postgresDB.STAGING_SCHEMA}.orders as o JOIN if_common.dim_dates cdd ON o.order_date = cdd.calendar_dt where day_of_the_week_num between 1 and 6 and not working_day limit 5",fetchall=True)
# query =f"""SELECT *
# FROM pg_depend
# WHERE objid = '{postgresDB.STAGING_SCHEMA}.orders'::regclass;
# """
# postgresDB.execute_query(query,fetchall=True)

#postgresDB.execute_query(f'GRANT ALL PRIVILEGES ON TABLE reviews TO {postgresDB.USERNAME}',fetchall=False)

#data.to_csv("all_schema.csv")
postgresDB.commit()
postgresDB.close()