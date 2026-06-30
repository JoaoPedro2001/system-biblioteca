from app.models.emprestimo import Emprestimo
from database import SessionLocal

def deletar_emprestimo(emprestimo_id):
    session = SessionLocal()
    emprestimo = session.query(Emprestimo).filter(Emprestimo.id == emprestimo_id).first()

    if not emprestimo:
        session.close()
        return {"erro": "Empréstimo não encontrado"}

    session.delete(emprestimo)
    session.commit()
    session.close()
    return {"mensagem": "Empréstimo deletado com sucesso"}