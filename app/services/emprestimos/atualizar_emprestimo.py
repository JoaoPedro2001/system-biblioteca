from datetime import timedelta

from app.models.emprestimo import Emprestimo
from app.models.livro import Livro

from database import SessionLocal

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

    livro = (
        session
        .query(Livro)
        .filter(Livro.id == emprestimo.livro_id)
        .first()
    )

    novo_status = data["status"]

    emprestimo.status = novo_status

    if data.get("renovar"):
        emprestimo.data_devolucao += timedelta(days=7)

    if novo_status == "devolvido":
        livro.status = "disponivel"

    session.commit()

    session.refresh(emprestimo)

    resultado = {
        "id": emprestimo.id,
        "status": emprestimo.status,
        "data_devolucao": emprestimo.data_devolucao
    }

    session.close()

    return resultado