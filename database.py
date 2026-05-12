from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from pathlib import Path

# Define que o arquivo .db será gerado na pasta do projeto 
BASE_DIR = Path(__file__).resolve().parent

# Pasta data
DATA_DIR = BASE_DIR / "data"

# Cria pasta data se não existir
DATA_DIR.mkdir(exist_ok=True)

# Nome do rquivo db criado no SQLite
DATABASE_NAME = "biblioteca_db.db"

# Caminho do banco SQLite
DATABASE_PATH = DATA_DIR / DATABASE_NAME

# URL do banco de dados
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

# Engine principal
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=True
)

# Criar seção local para operações do banco dedados
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base ORM
Base = declarative_base()

print(f"Banco de dados SQLite criado em: {DATABASE_PATH}")