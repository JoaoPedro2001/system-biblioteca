from app.models.bibliotecario import Bibliotecario
from database import SessionLocal

def buscar_bibliotecarios():
    session = SessionLocal()

    bibliotecarios = session.query(Bibliotecario)

    resultado = []

    for bibliotecario in bibliotecarios:
        resultado.append({
            "id": bibliotecario.id,
            "nome": bibliotecario.nome,
            "email": bibliotecario.email,
            "senha": bibliotecario.senha,
            "admin": bibliotecario.admin
        })

    session.close()

    return resultado


def buscar_bibliotecarios_por_id(bibliotecairo_id):
    session = SessionLocal()

    bibliotecario = (
        session
        .query(Bibliotecario)
        .filter(Bibliotecario.id == bibliotecairo_id)
        .first()
    )

    if not bibliotecario:
        session.close()
        return None
    
    resultado = {
        "id": bibliotecario.id,
        "nome": bibliotecario.nome,
        "email": bibliotecario.email,
        "senha": bibliotecario.senha,
        "admin":bibliotecario.admin
    }

    session.close()

    return resultado


def cadastrar_bibliotecario(data):
    session = SessionLocal()

    novo_bibliotecario = Bibliotecario(
        nome=data["nome"],
        email=data["email"],
        senha=data["senha"],
        admin=data["admin"]
    )

    session.add(novo_bibliotecario)

    session.commit()

    session.refresh(novo_bibliotecario)

    resultado = {
        "id": novo_bibliotecario.id,
        "nome": novo_bibliotecario.nome,
        "email": novo_bibliotecario.email,
        "senha": novo_bibliotecario.senha,
        "admin":novo_bibliotecario.admin
    }

    session.close()

    return resultado


def atualizar_bibliotecario(bibliotecairo_id, data):
    session = SessionLocal()

    bibliotecario = (
        session
        .query(Bibliotecario)
        .filter(Bibliotecario.id == bibliotecairo_id)
        .first()
    )

    if not bibliotecario:
        session.close()
        return None
    
    bibliotecario.nome=data["nome"]
    bibliotecario.email=data["email"]
    bibliotecario.senha=data["senha"]
    bibliotecario.admin=data["admin"]

    session.commit()

    session.refresh(bibliotecario)

    resultado = {
        "id": bibliotecario.id,
        "nome": bibliotecario.nome,
        "email": bibliotecario.email,
        "senha": bibliotecario.senha,
        "admin":bibliotecario.admin
    }

    session.close()

    return resultado


def deletar_bibliotecarios(bibliotecairo_id):
    session = SessionLocal()

    bibliotecario = (
        session
        .query(Bibliotecario)
        .filter(Bibliotecario.id == bibliotecairo_id)
        .first()   
    )

    if not bibliotecario:
        session.close()
        return None
    
    session.delete(bibliotecario)

    session.commit()

    session.close()

    return True