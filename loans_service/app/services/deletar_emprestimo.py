from app.models.emprestimo import Emprestimo
from database import SessionLocal


def deletar_emprestimo(emprestimo_id):
    session = SessionLocal()

    emprestimo = (
        session.query(Emprestimo)
        .filter(Emprestimo.id == emprestimo_id)
        .first()
    )

    if not emprestimo:
        session.close()
        return {"erro": "Empréstimo não encontrado"}

    # REGRA DE NEGÓCIO
    # Não permitir exclusão de empréstimos ativos

    if emprestimo.status == "emprestado":
        session.close()
        return {
            "erro": "Não é possível deletar um empréstimo ativo."
        }

    session.delete(emprestimo)
    session.commit()
    session.close()

    return {
        "mensagem": "Empréstimo deletado com sucesso."
    }