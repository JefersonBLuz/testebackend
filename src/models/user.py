from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship # Se houver relacionamentos futuros

from src.core.database import Base # Importa a Base declarativa

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)

    # Adicionar relacionamentos aqui se necessário no futuro
    # items = relationship("Item", back_populates="owner") 