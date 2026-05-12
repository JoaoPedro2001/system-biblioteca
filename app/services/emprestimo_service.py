from app.models.emprestimo import Emprestimo
from database import SessionLocal

from datetime import date

def buscar_emprestimos():
    session = SessionLocal()

    emprestimos = session.query(Emprestimo).all()

    resultado = []

    for emprestimo in emprestimos:
        resultado.append({
            "id": emprestimo.id,
            "livro_id": emprestimo.livro_id,
            "leitor_id": emprestimo.leitor_id,
            "bibliotecario_id": emprestimo.bibliotecario_id,
            "data_emprestimo": emprestimo.data_emprestimo,
            "data_devolucao": emprestimo.data_devolucao,
            "status": emprestimo.status
        })

    session.close()

    return resultado


def buscar_emprestimos_por_id(emprestimo_id):
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


def deletar_emprestimos(emprestimo_id):
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
    
    session.delete(emprestimo)

    session.commit()

    session.close()

    return True