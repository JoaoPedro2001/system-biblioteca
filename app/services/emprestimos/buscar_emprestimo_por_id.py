from app.models.emprestimo import Emprestimo
from database import SessionLocal

def buscar_emprestimo_por_id(emprestimo_id):
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
    
    resultado = {
        "id": emprestimo.id,
        "livro_id": emprestimo.livro_id,
        "leitor_id": emprestimo.leitor_id,
        "bibliotecario_id": emprestimo.bibliotecario_id,
        "data_emprestimo": emprestimo.data_emprestimo,
        "data_devolucao": emprestimo.data_devolucao,
        "status": emprestimo.status
    }

    session.close()

    return resultado