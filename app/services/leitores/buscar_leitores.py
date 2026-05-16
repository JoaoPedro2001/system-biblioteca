from app.models.leitor import Leitor
from database import SessionLocal

def buscar_leitores():
    session = SessionLocal()

    leitores = session.query(Leitor).all()

    resultado = []

    for leitor in leitores:
        resultado.append({
            "id": leitor.id,
            "nome": leitor.nome,
            "email":leitor.email,
            "telefone": leitor.telefone,
            "data_cadastro": leitor.data_cadastro
        })

    session.close()

    return resultado