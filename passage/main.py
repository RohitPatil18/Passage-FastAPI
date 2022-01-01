from alembic import context
from sqlalchemy.engine import create_engine
from fastapi import FastAPI

from .database import Base, engine

from .users.views import router as user_router
from .auth.views import router as auth_router


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router)
app.include_router(user_router)
