import json
from app.models.livro import Livro
from database import SessionLocal
from app.cache.redis_client import cache

CACHE_KEY = "livros:all"

def buscar_livros():
    cached = cache.get(CACHE_KEY)

    if cached:
        return json.loads(cached)

    session = SessionLocal()

    livros = session.query(Livro).all()

    resultado = [
    {
        "id": l.id,
        "titulo": l.titulo,
        "autor": l.autor,
        "isbn": l.isbn,
        "categoria": l.categoria,
        "status": l.status,
        "observacoes": l.observacoes
    }
    for l in livros
]

    cache.setex(CACHE_KEY, 60, json.dumps(resultado))  # TTL 60s

    session.close()
    return resultado