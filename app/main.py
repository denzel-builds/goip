from fastapi import FastAPI
from app.database import engine, Base
#Import the models so Base knows about them before creating the tables
from app.models import opportunity
from app.routers import opportunities

#Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="goip API")

# Include the opportunities router
app.include_router(opportunities.router)

@app.get("/")
def read_root():
    return {"message": "Hello World from goip!"}