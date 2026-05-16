from flask import jsonify, request
from app.services.livros.buscar_livros import buscar_livros
from app.services.livros.buscar_livro_por_id import buscar_livros_por_id
from app.services.livros.cadastrar_livro import cadastrar_livro
from app.services.livros.atualizar_livro import atualizar_livro
from app.services.livros.deletar_livro import detelar_livro

def listar_livros():
    livros = buscar_livros()

    return jsonify(livros)


def listar_livro_por_id(livro_id):
    livro = buscar_livros_por_id(livro_id)

    if not livro:
        return jsonify({
            "erro": "Livro não encontrado"
        }), 404
    
    return jsonify(livro), 200


def criar_livro():
    data = request.get_json()

    livro = cadastrar_livro(data)

    return jsonify(livro), 201


def editar_livro(livro_id):
    data = request.get_json()

    livro = atualizar_livro(livro_id, data)

    if not livro:
        return jsonify({
            "erro": "Livro não encontrado"
        }), 404
    
    
    return jsonify(livro), 200


def remover_livro(livro_id):
    removido = detelar_livro(livro_id)

    if not removido:
        return jsonify({
            "erro": "Livro não encontrado"
        }), 404
    
    return jsonify({
        "mensagem": "Livro removido com sucesso"
    }), 200