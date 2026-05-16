from app.models.bibliotecario import Bibliotecario
from database import SessionLocal

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