import requests
from datetime import date, timedelta

from app.models.emprestimo import Emprestimo
from database import SessionLocal

CATALOG_URL = "http://catalog_service:5002/livros"


def cadastrar_emprestimo(data):
    session = SessionLocal()

    livro_id = data["livro_id"]

    # REGRA DE NEGÓCIO 1
    # Não permitir empréstimo de livro indisponível

    livro_resp = requests.get(f"{CATALOG_URL}/{livro_id}")

    if livro_resp.status_code != 200:
        session.close()
        return {"erro": "Livro não encontrado"}

    livro = livro_resp.json()

    if livro["status"] != "disponivel":
        session.close()
        return {"erro": "Livro não está disponível para empréstimo"}

    # Criação do empréstimo
    data_emprestimo = date.today()
    data_devolucao = data_emprestimo + timedelta(days=7)

    novo_emprestimo = Emprestimo(
        livro_id=data["livro_id"],
        leitor_id=data["leitor_id"],
        bibliotecario_id=data["bibliotecario_id"],
        data_emprestimo=data_emprestimo,
        data_devolucao=data_devolucao,
        status="emprestado"
    )

    session.add(novo_emprestimo)

    # REGRA DE NEGÓCIO
    # Atualizar automaticamente o status do livro para
    # "emprestado" após a criação do empréstimo

    resposta = requests.put(
        f"{CATALOG_URL}/{livro_id}",
        json={
            "status": "emprestado"
        }
    )

    if resposta.status_code != 200:
        session.rollback()
        session.close()
        return {"erro": "Falha ao atualizar o status do livro"}

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