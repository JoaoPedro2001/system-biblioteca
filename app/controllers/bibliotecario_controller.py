from flask import jsonify, request
from app.services.bibliotecarios.buscar_bibliotecarios import buscar_bibliotecarios
from app.services.bibliotecarios.buscar_biliotecario_por_id import buscar_bibliotecario_por_id
from app.services.bibliotecarios.cadastrar_bibliotecario import cadastrar_bibliotecario
from app.services.bibliotecarios.atualizar_bibliotecario import atualizar_bibliotecario
from app.services.bibliotecarios.deletar_bibliotecario import deletar_bibliotecario

def listar_bibliotecarios():
    bibliotecarios = buscar_bibliotecarios()

    return jsonify(bibliotecarios)


def listar_bibliotecario_por_id(bibliotecario_id):
    bibliotecario = buscar_bibliotecario_por_id(bibliotecario_id)

    if not bibliotecario:
        return jsonify({
            "erro": "Bibliotecario não encontrado"
        }), 404

    return jsonify(bibliotecario), 200


def criar_bibliotecario():
    data = request.get_json()

    bibliotecario = cadastrar_bibliotecario(data)

    return jsonify(bibliotecario), 201

def editar_bibliotecario(bibliotecario_id):
    data = request.get_json()

    bibliotecario = atualizar_bibliotecario(bibliotecario_id, data)

    if not bibliotecario:
        return jsonify({
            "erro": "Bibliotecario não encontrado"
        }), 404
    
    return jsonify(bibliotecario), 200

def remover_bibliotecario(bibliotecario_id):
    removido = deletar_bibliotecario(bibliotecario_id)

    if not removido:
        return jsonify({
            "erro": "Bibliotecario não encontrado"
        }), 404
    
    return jsonify({
        "mensagem": "Bibliotecario removido com sucesso"
    }), 200