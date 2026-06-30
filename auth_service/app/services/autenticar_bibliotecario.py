from app.models.bibliotecario import Bibliotecario

from app.services.password_service import verificar_senha
from app.services.jwt_service import gerar_token

from database import SessionLocal


def autenticar_bibliotecario(email, senha):

    session = SessionLocal()

    bibliotecario = (
        session
        .query(Bibliotecario)
        .filter(Bibliotecario.email == email)
        .first()
    )

    if not bibliotecario:
        session.close()
        return None

    if not verificar_senha(senha, bibliotecario.senha):
        session.close()
        return None

    token = gerar_token(bibliotecario)

    session.close()

    return token