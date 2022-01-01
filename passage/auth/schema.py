from typing import Optional
from pydantic import BaseModel

from passage.users.schema import UserRead


class AuthToken(BaseModel):
    access_token: str
    token_type: Optional[str] = "Bearer"
    user: UserRead
