from app.models.leitor import Leitor
from database import SessionLocal

def deletar_leitor(leitor_id):
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