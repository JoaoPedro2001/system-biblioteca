from app.models.bibliotecario import Bibliotecario
from database import SessionLocal

def buscar_bibliotecario_por_id(bibliotecairo_id):
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