from app.models.livro import Livro
from database import SessionLocal

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