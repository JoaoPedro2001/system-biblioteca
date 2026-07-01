from datetime import date

from app.models.leitor import Leitor
from database import SessionLocal


def cadastrar_leitor(data):
    session = SessionLocal()

    # REGRA DE NEGÓCIO
    # Não permitir leitores com e-mail duplicado.

    leitor_existente = (
        session
        .query(Leitor)
        .filter(Leitor.email == data["email"])
        .first()
    )

    if leitor_existente:
        session.close()
        return {
            "erro": "Já existe um leitor cadastrado com este e-mail."
        }

    novo_leitor = Leitor(
        nome=data["nome"],
        email=data["email"],
        telefone=data["telefone"],
        data_cadastro=date.today()
    )

    session.add(novo_leitor)
    session.commit()
    session.refresh(novo_leitor)

    resultado = {
        "id": novo_leitor.id,
        "nome": novo_leitor.nome,
        "email": novo_leitor.email,
        "telefone": novo_leitor.telefone,
        "data_cadastro": novo_leitor.data_cadastro
    }

    session.close()

    return resultado