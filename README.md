# SASI PoC Backend

Backend PoC para o SASI.

Desenvolvido por: thallysvilemos@gmail.com

## Configuração e Execução

1.  **Criar Ambiente Virtual:**
    ```bash
    python -m venv .venv
    ```
2.  **Ativar Ambiente Virtual:**
    *   Windows (cmd/powershell):
        ```bash
        .\.venv\Scripts\activate
        ```
    *   Linux/macOS (bash/zsh):
        ```bash
        source ./.venv/bin/activate
        ```
3.  **Instalar Dependências:**
    ```bash
    pip install -r requirements.txt
    # Para desenvolvimento (inclui testes):
    # pip install -r requirements-dev.txt
    ```
4.  **Configurar Variáveis de Ambiente:**
    *   Copie o arquivo `.env.example` (se existir) para `.env`.
    *   Preencha as variáveis no arquivo `.env` (DATABASE_URL, SECRET_KEY, etc.).
5.  **Executar a Aplicação:**
    ```bash
    uvicorn src.main:app --reload
    ```
    A API estará disponível em [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Estrutura

*Descrição da estrutura do projeto será adicionada aqui.* 