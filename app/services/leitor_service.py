from app.models.leitor import Leitor
from database import SessionLocal

from datetime import date

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


def buscar_leitores_por_id(leitor_id):
    session = SessionLocal()

    leitor = (
        session
        .query(Leitor)
        .filter(Leitor.id == leitor_id)
        .first()
    )

    print(leitor)

    if not leitor:
        session.close()
        return None
    
    resultado = {
        "id": leitor.id,
        "nome": leitor.nome,
        "email": leitor.email,
        "telefone": leitor.telefone,
        "data_cadastro": leitor.data_cadastro
    }

    session.close()

    return resultado


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


def atualizar_leitor(leitor_id, data):
    session = SessionLocal()

    leitor = (
        session
        .query(Leitor)
        .filter(Leitor.id == leitor_id)
        .first()
    )

    if not leitor:
        session.close()
        return None
    
    leitor.nome=data["nome"]
    leitor.email=data["email"]
    leitor.telefone=data["telefone"]

    session.commit()

    session.refresh(leitor)

    resultado = {
        "id": leitor.id,
        "nome": leitor.nome,
        "email": leitor.email,
        "telefone": leitor.telefone,
        "data_cadastro": leitor.data_cadastro
    }

    session.close()

    return resultado


def deletar_leitores(leitor_id):
    session = SessionLocal()

    leitor = (
        session
        .query(Leitor)
        .filter(Leitor.id == leitor_id)
        .first()
    )

    if not leitor:
        session.close()
        return None

    session.delete(leitor)

    session.commit()

    session.close()

    return True