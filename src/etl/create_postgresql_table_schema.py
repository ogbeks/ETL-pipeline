import psycopg2
import pandas as pd
import configparser

# Create a ConfigParser object and read the configuration file
config = configparser.ConfigParser()
config.read('config/settings.ini')

USERNAME = config.get("database", "USERNAME")
PASSWORD = config.get("database", "PASSWORD")
HOST = config.get("database", "HOST")
PORT = int(config.get("database", "PORT"))
DB_NAME = config.get("database", "DB_NAME")
STAGING_SCHEMA = config.get("database", "STAGING_SCHEMA")


# connecting to PostgreSQL db
conn = psycopg2.connect(user=USERNAME, password=PASSWORD, host=HOST, port=PORT, database=DB_NAME)

# create a cursor object
cur = conn.cursor()

# execute a SQL query to set the search path to a specific schema
cur.execute(f"SET search_path TO {STAGING_SCHEMA};")

# execute a SQL query
cur.execute("SELECT * FROM information_schema.tables")
#cur.execute("SELECT * FROM if_common.dim_customers")
# fetch the results
results = cur.fetchall()

column_names = [desc[0] for desc in cur.description]

# print the results
df = pd.DataFrame(results, columns=column_names)
print(df)
# close the cursor and connection
cur.close()
conn.close()