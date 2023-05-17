import configparser

# Create a ConfigParser object and read the configuration file
config = configparser.ConfigParser()
config.read('config/settings.ini')

# Access the configuration settings
db_name = config.get('database', 'DB_NAME')
db_password = config.get('database', 'PASSWORD')
print(db_name)