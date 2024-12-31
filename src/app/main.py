from contextlib import contextmanager
from fastapi import FastAPI

from app.api import ping, notes
from app.db import database, engine, metadata

metadata.create_all(engine)

@contextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)


app.include_router(ping.router)
app.include_router(notes.router, prefix="/notes", tags=["notes"])
