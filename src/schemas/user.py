from pydantic import BaseModel, EmailStr
from typing import Optional

# --- Propriedades Base --- #
# Propriedades compartilhadas por todos os schemas relacionados ao User
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    # Adicionar outros campos comuns se necessário (ex: nome completo)

# --- Schemas para Criação --- #
# Propriedades recebidas via API na criação de um usuário
class UserCreate(UserBase):
    email: EmailStr # Email é obrigatório na criação
    password: str # Senha em texto plano recebida da API

# --- Schemas para Atualização --- #
# Propriedades recebidas via API na atualização de um usuário
class UserUpdate(UserBase):
    password: Optional[str] = None # Senha é opcional na atualização

# --- Schemas para Leitura (resposta da API) --- #
# Propriedades armazenadas no DB que podem ser lidas (sem a senha)
class UserInDBBase(UserBase):
    id: int
    email: EmailStr # Garante que o email está presente ao ler do DB

    class Config:
        from_attributes = True # Permite mapear atributos do modelo SQLAlchemy

# Schema principal para retornar dados do usuário via API (NÃO inclui a senha)
class User(UserInDBBase):
    pass

# Schema interno que inclui a senha hasheada (NÃO expor via API diretamente)
class UserInDB(UserInDBBase):
    hashed_password: str 