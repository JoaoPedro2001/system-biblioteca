from app.models.livro import Livro
from database import SessionLocal

def atualizar_livro(livro_id, data):
    session = SessionLocal()
    livro = session.query(Livro).filter(Livro.id == livro_id).first()

    if not livro:
        session.close()
        return None
    
    if "titulo" in data:
        livro.titulo = data["titulo"]

    if "autor" in data:
        livro.autor = data["autor"]

    if "isbn" in data:
        livro.isbn = data["isbn"]

    if "categoria" in data:
        livro.categoria = data["categoria"]

    if "status" in data:
        livro.status = data["status"]

    if "observacoes" in data:
        livro.observacoes = data["observacoes"]
    
    session.commit()
    session.refresh(livro)
    
    resultado = {
        "id": livro.id,
        "titulo": livro.titulo,
        "autor": livro.autor,
        "isbn": livro.isbn,
        "categoria": livro.categoria,
        "status": livro.status,
        "observacoes": livro.observacoes
    }
    session.close()
    return resultado