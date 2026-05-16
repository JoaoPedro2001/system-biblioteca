from app.models.livro import Livro
from database import SessionLocal

def buscar_livros_por_id(livro_id):
    session = SessionLocal()

    livro = (
        session
        .query(Livro)
        .filter(Livro.id == livro_id)
        .first()
    )

    if not livro:
        session.close()
        return None
    
    resultado = {
        "id": livro.id,
        "titulo": livro.titulo,
        "autor": livro.autor,
        "isbn": livro.isbn,
        "categoria": livro.categoria,
        "quantidade_total": livro.quantidade_total,
        "quantidade_disponivel": livro.quantidade_disponivel
    }

    session.close()

    return resultado