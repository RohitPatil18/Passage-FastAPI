from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session

from passage.database import get_db
from passage.users.models import User
from passage.utils import verify_password

from .schema import AuthToken
from .utils import create_access_token



router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)


@router.post("/login")
def login(
    form: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = db.query(User) \
            .filter(User.email == form.username) \
            .first()
    error_message = ""
    if not user:
        error_message = "Invalid username, User not found."
    elif not verify_password(form.password, user.password):
        error_message = "Invalid credentials."
    if error_message != "":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=error_message)
    token = create_access_token(user)
    return AuthToken(token=token, user=user)
    