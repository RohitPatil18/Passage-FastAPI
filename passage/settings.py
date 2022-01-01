from starlette.config import Config

config = Config('.env')

SECRET_KEY = config("SECRET_KEY")


JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# database
# DB_HOST = config("DB_HOST")
# DB_USER = config("DB_USER")
# DB_PASSWORD = config("DB_USER")
# DB_NAME = config("DB_USER")
# DB_PORT = config("DB_USER")

DATABASE_URI = "sqlite:///passage.db"