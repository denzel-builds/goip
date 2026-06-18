from fastapi import FastAPI
from app.database import engine, Base
#Import the models so Base knows about them before creating the tables
from app.models import opportunity

#Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="goip API")

@app.get("/")
def read_root():
    return {"message": "Hello World from goip!"}