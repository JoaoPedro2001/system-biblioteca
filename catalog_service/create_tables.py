from database import Base, engine
from app.models.leitor import Leitor
from app.models.livro import Livro

print("Criando tabelas do Catalog Service...")
Base.metadata.create_all(bind=engine)

print("Tabela criada com sucesso!")