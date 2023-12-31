# DATA2BOT DATA ENGINEERING ASSESSMENT
This repository details the Data2bot Data Engineering Assessment.

# MY APPROACH
Following the Assessment Guideline, The ETL pipeline was built using python and SQL queries only.
My simple approach was to have proper structure of directory to build the pipeline.
This implies that I will be making use of OOP python class and modules files, and SQL queries files stored in a structured file directory. 
My thought process can be summarized in the following steps;
1. Store all secret keys and credentials in config file (for data security)
2. Extract the raw data (orders, reviews, shipments_deliveries) from S3 buckets
3. Create a PostgreSQL Class that handles all the communications such as connection, reading data, loading data etc
4. Create the DDL queries for staging_schema tables and analytics schema tables
5. Implement the Module that handles the creation of the staging_schema tables and analytics_schema tables in the PostgreSQL DB
6. Implement the Module that handles the loading of the extracted raw data into the PostgreSQL DB Staging_schema instance
7. Create SQL queries for the analytics results
8. Implement the Modules that run the analytics results queries, load the data into the Analytic_schema instance and upload the result into S3 bucket Analytics_export


# FILE DIRECTORY EXPLAINED
The full file and directory on one view
```
├── README.md
├── config
│   └── settings.ini
├── data
│   ├── analytics
│   │   ├── agg_public_holiday.csv
│   │   ├── agg_shipments.csv
│   │   └── best_performing_product.csv
│   └── raw
│       ├── orders.csv
│       ├── reviews.csv
│       └── shipments_deliveries.csv
├── logs
├── main.py
├── requirements.txt
├── sql
│   ├── analytics
│   │   ├── agg_public_holiday.sql
│   │   ├── agg_shipments.sql
│   │   └── best_performing_product.sql
│   └── table_schema
│       ├── derived
│       │   ├── agg_public_holiday.sql
│       │   ├── agg_shipments.sql
│       │   └── best_performing_product.sql
│       └── fact
│           ├── orders.sql
│           ├── reviews.sql
│           └── shipments_deliveries.sql
├── src
│   ├── etl
│   │   ├── create_table.py
│   │   ├── extract.py
│   │   ├── load.py
│   │   └── transform.py
│   └── utils
│       └── database.py
└── tests
```
-- **Config** --\
  This contains the secret keys of AWS and PostgreSQL DB credentials in the settings.ini file. This is to avoid the credential revealed in source code and only made to be upload in the instance that host the ETL pipeline.
  
-- **Data** --\
  This folder is sub-divided into two directory called raw and analytics. The **raw** folder represent the data extracted from the S3 bucket while the **analytics** folder represent the data to be upload into the Analytics_export of the S3 bucket.

-- **SQL** --\
  This folder stores all the queries utilize in creating the tables and also writing our analytics results. From the above file structure, you will find the table_schema hold two folder that create the table schema for both our extracted data from S3 bucket and the the analytics table schemas.
  
-- **SRC** --\
  This house all the python script and is sub-divided into two folders **etl** and **utils**. The **etl** folder represent the python script that are responsible for all the Extract, Load and Transform operations. The **utils** represent the helper class that are used in the etl folder. The **Utils** folder only contain the database class that is responsible for the postgreSQL connections and all actions.
  

-- requirement.txt --\
  This is the list of all module that will be install for the smooth running of the ETL pipeline. !!! Please, ensure to run **pip install -r requirement.txt** on the virtual environment created.

-- main.py --\
This is the main program that run ETL pipeline.

# FUTURE IMPROVEMENT
This is a basic ETL pipeline, In a real projects, I will explore a robust procedure to run the ETL pipeline by utilizing tools such as Docker to set up the environment and my configuration setting will be stored in the DockerFile. Thus, I will only reference the credential using the system environment. Also, I will explore the use of Airflow to run the work orchestration that occassionally load the data into the PostgreSQL table.

For a robust Analytics, I will make use of DBT to build my analytics queries and running the process of further analytics answers to questions.





