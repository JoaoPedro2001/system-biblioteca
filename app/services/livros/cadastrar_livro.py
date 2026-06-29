from app.models.livro import Livro
from database import SessionLocal

def cadastrar_livro(data):
    session = SessionLocal()

    novo_livro = Livro(
        titulo=data["titulo"],
        autor=data["autor"],
        isbn=data["isbn"],
        categoria=data["categoria"],
        status=data.get("status", "disponivel"),
        observacoes=data.get("observacoes", "")
    )

    session.add(novo_livro)

    session.commit()

    session.refresh(novo_livro)

    resultado = {
        "id":novo_livro.id,
        "titulo": novo_livro.titulo,
        "autor":novo_livro.autor,
        "isbn": novo_livro.isbn,
        "categoria": novo_livro.categoria,
        "status": novo_livro.status,
        "observacoes": novo_livro.observacoes
    }

    session.close()

    return resultado