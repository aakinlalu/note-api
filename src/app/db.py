import os

from databases import Database
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Table,
    create_engine,
    MetaData
)
from sqlalchemy.sql import func

DATABASE_URL = os.getenv("DATABASE_URL")

# Define your table(s)
engine = create_engine(DATABASE_URL)
metadata = MetaData()
notes = Table(
    "notes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(50)),
    Column("description", String(50)),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)

# databases query builder
database = Database(DATABASE_URL)
