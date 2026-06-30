from database import Base, engine
from app.models.bibliotecario import Bibliotecario

print("Criando tabelas do Auth Service...")
Base.metadata.create_all(bind=engine)

print("Tabela criada com sucesso!")