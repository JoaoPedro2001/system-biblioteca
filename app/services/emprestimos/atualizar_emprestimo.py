from app.models.emprestimo import Emprestimo
from database import SessionLocal

from datetime import date

def atualizar_emprestimo(emprestimo_id, data):
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
    
    emprestimo.livro_id=data["livro_id"]
    emprestimo.leitor_id=data["leitor_id"]
    emprestimo.bibliotecario_id=data["bibliotecario_id"]
    emprestimo.data_emprestimo=date.fromisoformat(data["data_emprestimo"])
    emprestimo.data_devolucao=date.fromisoformat(data["data_devolucao"])
    emprestimo.status=data["status"]

    session.commit()

    session.refresh(emprestimo)

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