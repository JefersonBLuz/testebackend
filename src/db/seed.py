from sqlalchemy.orm import Session
from src.core.database import SessionLocal
from src.models.user import User
from src.auth.security import get_password_hash
from src.core.config import settings

def create_initial_superuser(db: Session) -> None:
    """Cria o usuário superuser inicial se ele não existir."""
    user = db.query(User).filter(User.email == "admin@admin.com").first()
    if not user:
        db_user = User(
            email="admin@admin.com",
            hashed_password=get_password_hash("admin123"),
            is_active=True,
            is_superuser=True
        )
        db.add(db_user)
        db.commit()
        print("Superuser criado com sucesso!")
    else:
        print("Superuser já existe!")

def init_db() -> None:
    """Inicializa o banco de dados com dados iniciais."""
    db = SessionLocal()
    try:
        create_initial_superuser(db)
    finally:
        db.close() 