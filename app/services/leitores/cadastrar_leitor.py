from app.models.leitor import Leitor
from database import SessionLocal

from datetime import date

def cadastrar_leitor(data):
    session = SessionLocal()

    novo_leitor = Leitor(
        nome=data["nome"],
        email=data["email"],
        telefone=data["telefone"],
        data_cadastro=date.today()
    )

    session.add(novo_leitor)

    session.commit()

    session.refresh(novo_leitor)

    reesultado = {
        "id": novo_leitor.id,
        "nome": novo_leitor.nome,
        "email": novo_leitor.email,
        "telefone": novo_leitor.telefone,
        "data_cadastro": novo_leitor.data_cadastro
    }

    session.close()

    return reesultado