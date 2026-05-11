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


def atualizar_livro(livro_id, data):
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
    
    livro.titulo=data["titulo"]
    livro.autor=data["autor"]
    livro.isbn=data["isbn"]
    livro.categoria=data["categoria"]
    livro.quantidade_total=data["quantidade_total"]
    livro.quantidade_disponivel=data["quantidade_disponivel"]
    
    session.commit()

    session.refresh(livro)
    
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


def detelar_livros(livro_id):
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
    
    session.delete(livro)

    session.commit()

    session.close()

    return True