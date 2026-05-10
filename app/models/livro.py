from sqlalchemy import (
    Column,
    Integer,
    String,
)

from database import Base, engine

class Livro(Base):
    __tablename__ = "livro"
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(200), nullable=False)
    autor = Column(String(150), nullable=False)
    isbn = Column(String(20), unique=True, nullable=False)
    categoria = Column(String(100))
    quantidade_total = Column(Integer, nullable=False)
    quantidade_disponivel = Column(Integer, nullable=False)