from database import Base, engine

from app.models.bibliotecario import Bibliotecario
from app.models.leitor import Leitor
from app.models.livro import Livro
from app.models.emprestimo import Emprestimo

# Registra as tabelas importadas e as cria em conjunto
Base.metadata.create_all(engine)

print("Tabelas criadas!")