from typing import Optional
from datetime import timedelta, datetime
from jose import JWTError, jwt

from passage.settings import SECRET_KEY, JWT_ALGORITHM, \
    ACCESS_TOKEN_EXPIRE_MINUTES



def create_access_token(
    payload: dict, expire_mins: Optional[int] = ACCESS_TOKEN_EXPIRE_MINUTES
):
    expire_aft = datetime.utcnow() + timedelta(minutes=expire_mins)
    payload.update({"exp": expire_aft})
    token = jwt.encode(payload, SECRET_KEY, algorithm=JWT_ALGORITHM)
    return token
