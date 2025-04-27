from sqlalchemy.orm import Session

from src.models.user import User
from src.schemas.user import UserCreate, UserUpdate
from src.auth.security import get_password_hash # Importaremos a função de hash depois

def get_user(db: Session, user_id: int) -> User | None:
    """Busca um usuário pelo ID."""
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str) -> User | None:
    """Busca um usuário pelo email."""
    return db.query(User).filter(User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[User]:
    """Busca múltiplos usuários com paginação."""
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate) -> User:
    """Cria um novo usuário no banco de dados."""
    hashed_password = get_password_hash(user.password)
    db_user = User(
        email=user.email,
        hashed_password=hashed_password,
        is_active=user.is_active,
        is_superuser=user.is_superuser
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, db_user: User, user_in: UserUpdate) -> User:
    """Atualiza um usuário existente."""
    user_data = user_in.model_dump(exclude_unset=True) # Pega só os campos enviados
    if "password" in user_data and user_data["password"]:
        hashed_password = get_password_hash(user_data["password"])
        db_user.hashed_password = hashed_password
        del user_data["password"] # Remove para não tentar setar diretamente

    for field, value in user_data.items():
        setattr(db_user, field, value)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Nota: A função delete_user pode ser adicionada se necessário.
# def delete_user(db: Session, user_id: int) -> User | None:
#     db_user = get_user(db, user_id=user_id)
#     if db_user:
#         db.delete(db_user)
#         db.commit()
#     return db_user 