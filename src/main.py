from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # Importa o middleware CORS
from src.core.config import settings
from src.api.v1.api import api_router as api_router_v1
from src.core.database import Base, engine
from src.db.seed import init_db

# Criar as tabelas do banco de dados
Base.metadata.create_all(bind=engine)

# Criar usuário inicial
init_db()

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json" # URL do Swagger UI
)

# Configurar CORS
# Ajuste as origens permitidas conforme necessário (ex: URL de produção depois)
origins = [
    "http://localhost:3001", # Frontend Next.js dev
    "http://127.0.0.1:3001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"], # Permite todos os headers
)

# Inclui o roteador da API v1
app.include_router(api_router_v1, prefix=settings.API_V1_STR)

@app.get("/", tags=["Root"])
async def read_root():
    """Endpoint raiz para verificar se a API está online."""
    return {"message": f"Welcome to {settings.PROJECT_NAME}"} 