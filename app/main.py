from fastapi import FastAPI

app = FastAPI(title="goip API")

@app.get("/")
def read_root():
    return {"message": "Hello World from goip!"}