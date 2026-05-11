from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
)

from app.database import Base, engine

class Bibliotecario(Base):
    __tablename__ = "bibliotecario"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    senha = Column(String(255), nullable=False)
    admin = Column(Boolean, default=False)