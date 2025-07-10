# main.py
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.routes import router
from app.db.database import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()

    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router)
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}



