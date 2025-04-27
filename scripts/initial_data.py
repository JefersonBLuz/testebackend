import logging

from sqlalchemy.orm import Session

from src.core.database import engine, Base, SessionLocal
from src.crud import crud_user
from src.schemas.user import UserCreate
from src.core.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Dados do superusuário inicial (exemplo)
# Pode ser movido para variáveis de ambiente em config.py se preferir
INITIAL_SUPERUSER_EMAIL = "admin@example.com"
INITIAL_SUPERUSER_PASSWORD = "changethis"

def init_db(db: Session) -> None:
    # Cria todas as tabelas definidas em Base (ex: users)
    logger.info("Criando tabelas...")
    Base.metadata.create_all(bind=engine)
    logger.info("Tabelas criadas.")

    # Cria o superusuário inicial, se não existir
    user = crud_user.get_user_by_email(db, email=INITIAL_SUPERUSER_EMAIL)
    if not user:
        logger.info(f"Criando superusuário inicial: {INITIAL_SUPERUSER_EMAIL}")
        user_in = UserCreate(
            email=INITIAL_SUPERUSER_EMAIL,
            password=INITIAL_SUPERUSER_PASSWORD,
            is_superuser=True,
            is_active=True
        )
        user = crud_user.create_user(db, user=user_in)
        logger.info("Superusuário criado.")
    else:
        logger.info("Superusuário inicial já existe.")

if __name__ == "__main__":
    logger.info("Iniciando criação da base de dados...")
    db = SessionLocal()
    init_db(db)
    db.close()
    logger.info("Base de dados inicializada.") 