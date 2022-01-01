from typing import List
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from passage.utils import get_password_hash

from .models import User


class UserService(object):

    def __init__(self, db: Session):
        self.db = db

    def create(self, data: dict) -> User:
        data['password'] = get_password_hash(data['password'])
        user = User(**data)
        self.db.add(user)
        self.db.commit()
        return user

    def get(self, id: int) -> User:
        user = self.db.query(User).get(id)
        return user

    def get_or_404(self, id: int) -> User:
        user = self.get(id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return user   

    def get_many(self) -> List[User]:
        return self.db.query(User).all()

    def delete(self, id) -> None:
        user = self.get_or_404(id)
        self.db.delete(user)
        self.db.commit()

    def update(self, id: int, data:str) -> User:
        user = self.get_or_404(id)
        for key, value in data.items():
            setattr(user, key, value)
        return user