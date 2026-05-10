from database import Base, engine

from models.bibliotecario import Bibliotecario
from models.leitor import Leitor
from models.livro import Livro
from models.emprestimo import Emprestimo

# Registra as tabelas importadas e as cria em conjunto
Base.metadata.create_all(engine)

print("Tabelas criadas!")