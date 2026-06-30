from database import Base, engine
from app.models.emprestimo import Emprestimo

print("Criando tabelas do Loans Service...")
Base.metadata.create_all(bind=engine)

print("Tabela de emprestimos criada com sucesso!")