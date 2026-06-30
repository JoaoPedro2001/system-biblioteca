from sqlalchemy import Column, Integer, String
from database import Base

class Livro(Base):
    __tablename__ = "livro"
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(200), nullable=False)
    autor = Column(String(150), nullable=False)
    isbn = Column(String(20), nullable=False)
    categoria = Column(String(100))
    status = Column(String(30), nullable=False, default="disponivel")
    observacoes = Column(String(500))