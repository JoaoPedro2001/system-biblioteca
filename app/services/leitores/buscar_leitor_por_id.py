from app.models.leitor import Leitor
from database import SessionLocal

def buscar_leitor_por_id(leitor_id):
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