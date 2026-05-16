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