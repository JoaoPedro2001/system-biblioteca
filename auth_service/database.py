import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Lê a URL de conexão injetada no docker-compose.yml
# Exemplo: postgresql://postgres:postgres@postgres:5432/biblioteca_db
DATABASE_URL = os.environ.get("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("A variável de ambiente DATABASE_URL não foi definida!")

engine = create_engine(
    DATABASE_URL,
    echo=True,     # Mostra o SQL gerado no console do Docker (ótimo para debug)
    future=True
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)

Base = declarative_base()

# Helper útil para usar nas rotas/controllers com o bloco 'with'
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()