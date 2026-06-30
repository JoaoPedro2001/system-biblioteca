import bcrypt


def gerar_hash(senha):
    return bcrypt.hashpw(
        senha.encode(),
        bcrypt.gensalt()
    ).decode()


def verificar_senha(senha, senha_hash):
    return bcrypt.checkpw(
        senha.encode(),
        senha_hash.encode()
    )