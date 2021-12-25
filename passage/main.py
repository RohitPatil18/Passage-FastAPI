from fastapi import FastAPI
from sqlalchemy.engine import create_engine

from .database import Base, engine
from .users.views import router as user_router


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router)