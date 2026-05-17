from app.models.emprestimo import Emprestimo
from database import SessionLocal

from datetime import timedelta

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

    emprestimo.status = data["status"]

    if data.get("renovar"):

        emprestimo.data_devolucao = (
            emprestimo.data_devolucao + timedelta(days=7)
        )

    session.commit()

    session.refresh(emprestimo)

    resultado = {
        "data_devolucao": emprestimo.data_devolucao,
        "status": emprestimo.status
    }

    session.close()

    return resultado