from app.models.emprestimo import Emprestimo
from database import SessionLocal

from datetime import date

def cadastrar_emprestimo(data):
    session = SessionLocal()

    novo_emprestimo = Emprestimo(
        livro_id=data["livro_id"],
        leitor_id=data["leitor_id"],
        bibliotecario_id=data["bibliotecario_id"],

        data_emprestimo=date.fromisoformat(
            data["data_emprestimo"]
        ),
        
        data_devolucao=date.fromisoformat(
            data["data_devolucao"]
        ),
        
        status=data["status"]
    )

    session.add(novo_emprestimo)

    session.commit()

    session.refresh(novo_emprestimo)

    resultado = {
        "id": novo_emprestimo.id,
        "livro_id": novo_emprestimo.livro_id,
        "leitor_id": novo_emprestimo.leitor_id,
        "bibliotecario_id": novo_emprestimo.bibliotecario_id,
        "data_emprestimo": novo_emprestimo.data_emprestimo,
        "data_devolucao": novo_emprestimo.data_devolucao,
        "status": novo_emprestimo.status
    }

    session.close()

    return resultado