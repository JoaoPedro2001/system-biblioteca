from app.models.livro import Livro
from database import SessionLocal

def detelar_livro(livro_id):
    session = SessionLocal()

    livro = (
        session
        .query(Livro)
        .filter(Livro.id == livro_id)
        .first()
    )

    if not livro:
        session.close()
        return None
    
    session.delete(livro)

    session.commit()

    session.close()

    return True