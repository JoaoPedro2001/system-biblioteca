from app.models.livro import Livro
from database import SessionLocal
from app.cache.redis_client import cache


def deletar_livro(livro_id):
    session = SessionLocal()

    livro = (
        session.query(Livro)
        .filter(Livro.id == livro_id)
        .first()
    )

    if not livro:
        session.close()
        return None

    # REGRA DE NEGÓCIO
    # Não permitir exclusão de livros emprestados

    if livro.status == "emprestado":
        session.close()
        return {
            "erro": "Livro não pode ser deletado porque está emprestado."
        }

    session.delete(livro)
    session.commit()
    cache.delete("livros:all")
    cache.delete(f"livro:{livro_id}")
    session.close()

    return {
        "mensagem": "Livro deletado com sucesso."
    }