from app.models.bibliotecario import Bibliotecario
from database import SessionLocal

def deletar_bibliotecario(bibliotecairo_id):
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