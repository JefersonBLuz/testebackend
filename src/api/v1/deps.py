from typing import Generator, Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from src.core.database import get_db
from src.models.user import User
from src.schemas.token import TokenData
from src.crud import crud_user
from src.auth import security

# Define o esquema de segurança OAuth2 (pega o token do header Authorization: Bearer <token>)
# O tokenUrl deve apontar para o endpoint de login que criaremos
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login/access-token")

def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
) -> User:
    """Dependência para obter o usuário atual a partir do token JWT."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data = security.decode_token(token)
    if not token_data or not token_data.sub:
        raise credentials_exception

    # Assumindo que 'sub' contém o email do usuário
    user = crud_user.get_user_by_email(db, email=token_data.sub)
    if user is None:
        raise credentials_exception
    return user

def get_current_active_user(
    current_user: User = Depends(get_current_user)
) -> User:
    """Dependência para obter o usuário atual ATIVO."""
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

def get_current_active_superuser(
    current_user: User = Depends(get_current_active_user)
) -> User:
    """Dependência para obter o usuário atual ATIVO e SUPERUSER."""
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=403,
            detail="The user doesn't have enough privileges"
        )
    return current_user 