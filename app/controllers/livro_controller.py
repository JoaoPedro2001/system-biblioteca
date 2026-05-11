from flask import jsonify, request
from app.services.livro_service import(
    buscar_livros,
    cadastrar_livro
)

def listar_livros():
    livros = buscar_livros()

    return jsonify(livros)

def criar_livro():
    data = request.get_json()

    livro = cadastrar_livro(data)

    return jsonify(livro), 201