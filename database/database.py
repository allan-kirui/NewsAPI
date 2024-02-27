from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configparser import ConfigParser
from contextlib import contextmanager


class Database:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self):
        if self.__initialized:
            return

        self.__initialized = True

        # Read the config file
        config = ConfigParser()
        config.read("config.ini")

        # Extract the database connection details
        self.user = config.get("database", "user")
        self.password = config.get("database", "password")
        self.host = config.get("database", "host")
        self.database = config.get("database", "database")

        # Create the database URL
        self.DATABASE_URL = f"postgresql://{self.user}:{self.password}@{self.host}/{self.database}"

        self.engine = create_engine(self.DATABASE_URL, echo=True)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_db(self):
        db = self.SessionLocal()
        try:
            return db
        finally:
            db.close()
