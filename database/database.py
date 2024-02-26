from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configparser import ConfigParser

# Read the config file
config = ConfigParser()
config.read("config.ini")

# Extract the database connection details
user = config.get("database", "user")
password = config.get("database", "password")
host = config.get("database", "host")
database = config.get("database", "database")

# Create the database URL
DATABASE_URL = f"postgresql://{user}:{password}@{host}/{database}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()
