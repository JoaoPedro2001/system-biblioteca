from flask import jsonify, request
from app.services.leitores.buscar_leitores import buscar_leitores
from app.services.leitores.buscar_leitor_por_id import buscar_leitor_por_id
from app.services.leitores.cadastrar_leitor import cadastrar_leitor
from app.services.leitores.atualizar_leitor import atualizar_leitor
from app.services.leitores.deletar_leitor import deletar_leitor

def listar_leitores():
    leitores = buscar_leitores()

    return jsonify(leitores)


def listar_leitor_por_id(leitor_id):
    leitor = buscar_leitor_por_id(leitor_id)

    if not leitor:
        return jsonify({
            "erro": "Leitor não encontrado"
        }), 404
    
    return jsonify(leitor), 200


def criar_leitor():
    data = request.get_json()

    leitor = cadastrar_leitor(data)

    return jsonify(leitor), 201


def editar_leitor(leitor_id):
    data = request.get_json()

    leitor = atualizar_leitor(leitor_id, data)

    if not leitor:
        return jsonify({
            "erro": "Leitor não encontrado"
        }), 404
    
    return jsonify(leitor), 200


def remover_leitor(leitor_id):
    removido  = deletar_leitor(leitor_id)

    if not removido:
        return jsonify({
            "erro": "Leitor não encontrado"
        }), 404
    
    return jsonify({
        "mensagem": "Leitor removido com sucesso"
    }), 200