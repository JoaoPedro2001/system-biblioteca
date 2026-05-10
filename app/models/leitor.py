from sqlalchemy import (
    Column,
    Integer,
    String,
    Date
)

from database import Base, engine

class Leitor(Base):
    __tablename__ = "leitor"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    telefone = Column(String(20))
    data_cadastro = Column(Date)