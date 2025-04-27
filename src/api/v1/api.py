from fastapi import APIRouter
# Importar endpoints específicos
from src.api.v1.endpoints import users, login # Descomentado

api_router = APIRouter()

# Incluir roteadores dos endpoints
api_router.include_router(login.router, tags=["Login"]) # Tag ajustada
api_router.include_router(users.router, prefix="/users", tags=["Users"]) # Tag ajustada

# Placeholder para outros endpoints da v1 (ex: indicadores, estabelecimentos)
@api_router.get("/health", tags=["Health"])
async def health_check():
    return {"status": "OK"} 