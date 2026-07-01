import requests
from datetime import timedelta

from app.models.emprestimo import Emprestimo
from database import SessionLocal

CATALOG_URL = "http://catalog_service:5002/livros"


def atualizar_emprestimo(emprestimo_id, data):
    session = SessionLocal()

    emprestimo = (
        session.query(Emprestimo)
        .filter(Emprestimo.id == emprestimo_id)
        .first()
    )

    if not emprestimo:
        session.close()
        return None

    novo_status = data["status"]

    status_anterior = emprestimo.status

    emprestimo.status = novo_status

    # Permitir renovação do empréstimo por mais 7 dias
    if data.get("renovar"):
        emprestimo.data_devolucao += timedelta(days=7)

    # REGRA DE NEGÓCIO
    # Atualizar automaticamente o status do livro para
    # "disponivel" quando o empréstimo for devolvido
    
    if status_anterior != "devolvido" and novo_status == "devolvido":

        resposta = requests.put(
            f"{CATALOG_URL}/{emprestimo.livro_id}",
            json={
                "status": "disponivel"
            }
        )

        if resposta.status_code != 200:
            session.close()
            return {
                "erro": "Falha ao atualizar o status do livro."
            }

    session.commit()
    session.refresh(emprestimo)

    resultado = {
        "id": emprestimo.id,
        "status": emprestimo.status,
        "data_devolucao": emprestimo.data_devolucao
    }

    session.close()

    return resultado