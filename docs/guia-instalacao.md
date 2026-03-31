# Guia de Instalação

Guia rápido para configurar o ConectaTalentos.

## Instalação

1. Clone o repositório
2. Crie ambiente virtual: `python -m venv .venv`
3. Ative: `.venv\Scripts\activate` (Windows) ou `source .venv/bin/activate` (Linux/Mac)
4. Instale dependências: `pip install -r requirements.txt`
5. Configure `.env` (copie de `.env.example`)
6. Inicialize banco: `python -c "from app.database import init_db; init_db()"`
7. Execute: `python run.py`

Acesse: http://localhost:8000

## Testes

```bash
pytest tests/
pytest tests/ --cov=app --cov=backend/src
```
