import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

#Load environment variables from .env file
load_dotenv()

# Get the database URL
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

#Create the engine (the actual connection to Postgres)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#The Base class that all our database models will inherit from  
Base = declarative_base()

#Dependency to get a database session in our router
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()