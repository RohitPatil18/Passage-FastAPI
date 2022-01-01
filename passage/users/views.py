from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm.session import Session

from passage.database import get_db

from .schema import UserCreate, UserRead, UserUpdate
from .services import UserService


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("", response_model=List[UserRead])
async def get_users_list(db: Session = Depends(get_db)):
    users_list = UserService(db).get_many()
    return users_list


@router.post(
    "", 
    status_code=status.HTTP_201_CREATED,
    response_model=UserRead
)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user =  UserService(db).create(user.dict())
    return user


@router.get("/{id}", response_model=UserRead)
async def get_user(id: int, db: Session = Depends(get_db)):
    user = UserService(db).get_or_404(id)
    return user


@router.put("/{id}", response_model=UserRead)
async def update_user(id: int, user: UserUpdate, db: Session = Depends(get_db)):
    user = UserService(db).update(id, user.dict())
    return user


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def get_user(id: int, db: Session = Depends(get_db)):
    UserService(db).delete(id)


