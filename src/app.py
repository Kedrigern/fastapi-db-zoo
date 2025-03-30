from contextlib import asynccontextmanager
from fastapi import FastAPI
from .database.connection import create_db_and_tables
from .routers.pet import pets_router
from .routers.kind import kind_router


@asynccontextmanager
async def life_span(_: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(name="ZOO", lifespan=life_span)


@app.get("/")
def hello():
    return {"detail": "Hello world"}


app.include_router(pets_router, prefix="/pet")
app.include_router(kind_router, prefix="/kind")
