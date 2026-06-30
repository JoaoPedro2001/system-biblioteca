from app.models.bibliotecario import Bibliotecario
from app.services.password_service import gerar_hash
from database import SessionLocal

def atualizar_bibliotecario(bibliotecario_id, data):
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
    
    bibliotecario.nome = data["nome"]
    bibliotecario.email = data["email"]

    if "senha" in data:
        bibliotecario.senha = gerar_hash(data["senha"])
    
    bibliotecario.admin = data["admin"]

    session.commit()
    session.refresh(bibliotecario)

    resultado = {
        "id": bibliotecario.id,
        "nome": bibliotecario.nome,
        "email": bibliotecario.email,
        "admin": bibliotecario.admin
    }

    session.close()
    return resultado