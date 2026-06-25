from fastapi import FastAPI
from app.database import engine, Base
#Import the models so Base knows about them before creating the tables
from app.models import opportunity, user, application
from app.routers import auth, opportunities, applications, users

#Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="goip API")

app.include_router(auth.router)
# Include the opportunities router
app.include_router(opportunities.router)
app.include_router(applications.router)
app.include_router(users.router)

@app.get("/")
def read_root():
    return {"message": "Hello World from goip!"}