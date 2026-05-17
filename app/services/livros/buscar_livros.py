from app.models.livro import Livro
from database import SessionLocal

def buscar_livros():
    session = SessionLocal()

    livros = session.query(Livro).all()

    resultado = []

    for livro in livros:
        resultado.append({
            "id": livro.id,
            "titulo": livro.titulo,
            "autor": livro.autor,
            "isbn": livro.isbn,
            "categoria": livro.categoria,
            "quantidade_total": livro.quantidade_total,
            "quantidade_disponivel": livro.quantidade_disponivel
        })

    session.close()

    return resultado