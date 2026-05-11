from flask import jsonify, request
from app.services.leitor_service import(
    buscar_leitores,
    buscar_leitores_por_id,
    cadastrar_leitor,
    atualizar_leitor,
    deletar_leitores,
)

def listar_leitores():
    leitores = buscar_leitores()

    return jsonify(leitores)


def listar_leitor_por_id(leitor_id):
    leitor = buscar_leitores_por_id(leitor_id)

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
    removido  = deletar_leitores(leitor_id)

    if not removido:
        return jsonify({
            "erro": "Leitor não encontrado"
        }), 404
    
    return jsonify({
        "mensagem": "Leitor removido com sucesso"
    }), 200