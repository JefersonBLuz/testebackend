from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.core.database import get_db
from src.schemas import user as user_schemas # Renomeado para evitar conflito
from src.crud import crud_user
from src.api.v1 import deps # Importa as dependências
from src.models.user import User as UserModel # Importa o modelo

router = APIRouter()

@router.post("/", response_model=user_schemas.User, status_code=status.HTTP_201_CREATED)
def create_user(
    *, # Força argumentos nomeados
    db: Session = Depends(get_db),
    user_in: user_schemas.UserCreate,
    # Descomentar para exigir superusuário para criar usuários:
    # current_user: UserModel = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Cria um novo usuário.
    (Aberto para qualquer um criar por enquanto, ajustar dependência para restringir)
    """
    user = crud_user.get_user_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )
    user = crud_user.create_user(db=db, user=user_in)
    return user

@router.get("/me", response_model=user_schemas.User)
def read_user_me(
    current_user: UserModel = Depends(deps.get_current_active_user),
) -> Any:
    """
    Obtém informações do usuário logado.
    """
    return current_user

# TODO: Adicionar endpoints para listar, atualizar, deletar usuários (protegidos)
# @router.get("/", response_model=List[user_schemas.User])
# def read_users(...):

# @router.get("/{user_id}", response_model=user_schemas.User)
# def read_user_by_id(...):

# @router.put("/{user_id}", response_model=user_schemas.User)
# def update_user(...): 