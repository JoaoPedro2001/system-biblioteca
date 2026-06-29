from app.models.emprestimo import Emprestimo
from app.models.livro import Livro
from database import SessionLocal

def deletar_emprestimo(emprestimo_id):
    session = SessionLocal()

    emprestimo = (
        session
        .query(Emprestimo)
        .filter(Emprestimo.id == emprestimo_id)
        .first()
    )

    if not emprestimo:
        session.close()
        return None
    
    livro = (
        session
        .query(Livro)
        .filter(Livro.id == emprestimo.livro_id)
        .first()
    )

    if livro:
        livro.status = "disponivel"

    session.delete(emprestimo)

    session.commit()

    session.close()

    return True