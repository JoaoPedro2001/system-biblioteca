from app.models.livro import Livro
from database import SessionLocal

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