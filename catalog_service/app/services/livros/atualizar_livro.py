from app.models.livro import Livro
from database import SessionLocal

def atualizar_livro(livro_id, data):
    session = SessionLocal()
    livro = session.query(Livro).filter(Livro.id == livro_id).first()

    if not livro:
        session.close()
        return None
    
    livro.titulo = data["titulo"]
    livro.autor = data["autor"]
    livro.isbn = data["isbn"]
    livro.categoria = data["categoria"]
    livro.status = data["status"]
    livro.observacoes = data.get("observacoes", "")
    
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