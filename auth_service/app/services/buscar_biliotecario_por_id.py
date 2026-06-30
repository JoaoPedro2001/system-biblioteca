from app.models.bibliotecario import Bibliotecario
from database import SessionLocal

def buscar_bibliotecario_por_id(bibliotecario_id):
    session = SessionLocal()

    bibliotecario = (
        session
        .query(Bibliotecario)
        .filter(Bibliotecario.id == bibliotecario_id)
        .first()
    )

    if not bibliotecario:
        session.close()
        return None
    
    resultado = {
        "id": bibliotecario.id,
        "nome": bibliotecario.nome,
        "email": bibliotecario.email,
        "admin": bibliotecario.admin
    }

    session.close()
    return resultado