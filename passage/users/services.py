from typing import List
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from passage.utils import get_password_hash

from .models import User


class UserService(object):

    def __init__(self, db: Session):
        self.db = db

    async def create(self, data: dict) -> User:
        data['password'] = get_password_hash(data['password'])
        user = User(**data)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    async def get(self, id: int) -> User:
        user = self.db.query(User).get(id)
        return user

    async def get_or_404(self, id: int) -> User:
        user = self.get(int)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return user   

    async def get_many(self) -> List[User]:
        return self.db.query(User).all()

    async def delete(self, id) -> None:
        user = await self.get_or_404(id)
        self.db.delete(user)
        self.db.commit()

    async def update(self, id: int, data:str) -> User:
        user = await self.get_or_404(id)
        for key, value in data.items():
            setattr(user, key, value)
        self.db.commit()
        return user