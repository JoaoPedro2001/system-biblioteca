import json
from app.models.livro import Livro
from database import SessionLocal
from app.cache.redis_client import cache

def buscar_livros_por_id(livro_id):
    key = f"livro:{livro_id}"

    cached = cache.get(key)
    if cached:
        return json.loads(cached)

    session = SessionLocal()

    livro = session.query(Livro).filter(Livro.id == livro_id).first()

    if not livro:
        session.close()
        return None

    resultado = {
        "id": livro.id,
        "titulo": livro.titulo,
        "autor": livro.autor,
        "isbn": livro.isbn,
        "categoria": livro.categoria,
        "status": livro.status,
        "observacoes": livro.observacoes
    }

    cache.setex(key, 60, json.dumps(resultado))

    session.close()
    return resultado