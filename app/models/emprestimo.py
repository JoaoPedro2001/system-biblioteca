from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    ForeignKey
)

from database import Base, engine
from models.livro import Livro
from models.leitor import Leitor
from models.bibliotecario import Bibliotecario

class Emprestimo(Base):
    __tablename__ = "emprestimo"
    id = Column(Integer, primary_key=True, autoincrement=True)
    livro_id = Column(Integer, ForeignKey("livro.id"))
    leitor_id = Column(Integer, ForeignKey("leitor.id"))
    bibliotecario_id = Column(Integer, ForeignKey("bibliotecario.id"))
    data_emprestimo = Column(Date, nullable=False)
    data_devolucao = Column(Date)
    status = Column(String(20), nullable=False)