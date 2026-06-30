from flask import jsonify, request

from app.services.autenticar_bibliotecario import autenticar_bibliotecario


def login():

    data = request.get_json()

    if not data:
        return jsonify({"erro": "Dados não enviados"}), 400

    email = data.get("email")
    senha = data.get("senha")

    if not email or not senha:
        return jsonify({"erro": "Email e senha são obrigatórios"}), 400

    token = autenticar_bibliotecario(email, senha)

    if token is None:
        return jsonify({"erro": "Email ou senha inválidos"}), 401

    return jsonify({
        "token": token
    }), 200