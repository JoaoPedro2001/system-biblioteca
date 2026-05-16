from app.models.leitor import Leitor
from database import SessionLocal

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