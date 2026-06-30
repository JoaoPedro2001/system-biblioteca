from sqlalchemy import Column, Integer, String, Date, ForeignKey
from database import Base

class Emprestimo(Base):
    __tablename__ = "emprestimo"

    id = Column(Integer, primary_key=True, index=True)
    
    livro_id = Column(Integer, nullable=False)
    leitor_id = Column(Integer, nullable=False)
    bibliotecario_id = Column(Integer, nullable=False)
    data_emprestimo = Column(Date, nullable=False)
    data_devolucao = Column(Date, nullable=True)
    status = Column(String(20), default="Ativo")