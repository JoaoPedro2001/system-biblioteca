import requests
from app.models.leitor import Leitor
from database import SessionLocal

LOANS_URL = "http://loans_service:5003/emprestimos"


def deletar_leitor(leitor_id):
    session = SessionLocal()

    leitor = (
        session
        .query(Leitor)
        .filter(Leitor.id == leitor_id)
        .first()
    )

    if not leitor:
        session.close()
        return None
    
    # REGRA DE NEGÓCIO
    # Não permitir excluir leitor com empréstimos ativos.
    try:
        resposta = requests.get(LOANS_URL)

        if resposta.status_code == 200:
            emprestimos = resposta.json()

            possui_emprestimo_ativo = any(
                emprestimo["leitor_id"] == leitor_id
                and emprestimo["status"] == "emprestado"
                for emprestimo in emprestimos
            )

            if possui_emprestimo_ativo:
                session.close()
                return {
                    "erro": (
                        "Leitor possui empréstimos ativos e não pode ser removido."
                    )
                }

    except requests.RequestException:
        session.close()
        return {
            "erro": (
                "Não foi possível verificar os empréstimos do leitor."
            )
        }

    session.delete(leitor)
    session.commit()
    session.close()

    return True