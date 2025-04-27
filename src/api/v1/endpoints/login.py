from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm # Formulário padrão para login
from sqlalchemy.orm import Session

from src.core.database import get_db
from src.schemas.token import Token
from src.crud import crud_user
from src.auth import security
from src.core.config import settings

router = APIRouter()

@router.post("/login/access-token", response_model=Token)
def login_access_token(
    db: Session = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests.

    Recebe username (email) e password via form data.
    """
    user = crud_user.get_user_by_email(db, email=form_data.username) # form_data usa 'username'
    if not user or not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        subject=user.email, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# TODO: Adicionar endpoint para testar o token (ex: /login/test-token)
# @router.post("/login/test-token", response_model=schemas.User)
# def test_token(current_user: models.User = Depends(deps.get_current_user)) -> Any:
#     """
#     Test access token
#     """
#     return current_user 