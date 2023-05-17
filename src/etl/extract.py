import boto3
from botocore import UNSIGNED
from botocore.client import Config
import configparser

# Create a ConfigParser object and read the configuration file
config = configparser.ConfigParser()
config.read('config/settings.ini')

# Access the configuration settings
bucket_name =config.get('AWS', 'BUCKET_NAME')

s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))
response = s3.list_objects(Bucket=bucket_name, Prefix="orders_data")

# downloading all files
s3.download_file(bucket_name, "orders_data/orders.csv", "data/raw/orders.csv")

s3.download_file(bucket_name, "orders_data/shipment_deliveries.csv", "data/raw/shipment_deliveries.csv")

s3.download_file(bucket_name, "orders_data/reviews.csv", "data/raw/reviews.csv")
