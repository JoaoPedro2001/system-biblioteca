import os
import jwt

from datetime import datetime, timedelta

SECRET_KEY = os.getenv("JWT_SECRET")

def gerar_token(bibliotecario):

    payload = {
        "id": bibliotecario.id,
        "nome": bibliotecario.nome,
        "email": bibliotecario.email,
        "admin": bibliotecario.admin,
        "exp": datetime.utcnow() + timedelta(hours=8)
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm="HS256"
    )


def validar_token(token):

    try:
        return jwt.decode(
            token,
            SECRET_KEY,
            algorithms=["HS256"]
        )

    except jwt.ExpiredSignatureError:
        return None

    except jwt.InvalidTokenError:
        return None