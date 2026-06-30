from app.models.bibliotecario import Bibliotecario
from app.services.password_service import gerar_hash
from database import SessionLocal

def cadastrar_bibliotecario(data):
    session = SessionLocal()

    novo_bibliotecario = Bibliotecario(
        nome=data["nome"],
        email=data["email"],
        senha=gerar_hash(data["senha"]),
        admin=data["admin"]
    )

    session.add(novo_bibliotecario)
    session.commit()
    session.refresh(novo_bibliotecario)

    resultado = {
        "id": novo_bibliotecario.id,
        "nome": novo_bibliotecario.nome,
        "email": novo_bibliotecario.email,
        "admin": novo_bibliotecario.admin
    }

    session.close()
    return resultado