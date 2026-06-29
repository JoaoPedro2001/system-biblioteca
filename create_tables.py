from database import Base, engine

from app.models.bibliotecario import Bibliotecario
from app.models.leitor import Leitor
from app.models.livro import Livro
from app.models.emprestimo import Emprestimo

Base.metadata.create_all(bind=engine)

print("Banco criado com sucesso.")