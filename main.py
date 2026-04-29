from fastapi import FastAPI
from api.routes import router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the Review Handling System API!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(router)