from pydantic import BaseModel
from typing import Optional

# Schema para os dados contidos no payload do JWT (o campo 'sub')
class TokenData(BaseModel):
    sub: Optional[str] = None # 'sub' (subject) geralmente armazena o ID ou email do usuário

# Schema para a resposta do endpoint de login
class Token(BaseModel):
    access_token: str
    token_type: str 