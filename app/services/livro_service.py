from app.models.livro import Livro
from app.database import SessionLocal

def buscar_livros():
    session = SessionLocal()

    livros = session.query(Livro).all()

    resultado = []

    for livro in livros:
        resultado.append({
            "id": livro.id,
            "titulo": livro.titulo,
            "autor": livro.autor,
            "isbn": livro.isbn
        })

    session.close()

    return resultado

def cadastrar_livro(data):
    session = SessionLocal()

    novo_livro = Livro(
        titulo=data["titulo"],
        autor=data["autor"],
        isbn=data["isbn"],
        categoria=data["categoria"],
        quantidade_total=data["quantidade_total"],
        quantidade_disponivel=data["quantidade_disponivel"]
    )

    session.add(novo_livro)

    session.commit()

    session.refresh(novo_livro)

    resultado = {
        "id":novo_livro.id,
        "titulo": novo_livro.titulo,
        "autor":novo_livro.autor,
        "isbn": novo_livro.isbn,
    }

    session.close()

    return resultado