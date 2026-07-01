from flask import jsonify, request
from app.services.buscar_emprestimos import buscar_emprestimos
from app.services.buscar_emprestimo_por_id import buscar_emprestimo_por_id
from app.services.cadastrar_emprestimo import cadastrar_emprestimo
from app.services.atualizar_emprestimo import atualizar_emprestimo
from app.services.deletar_emprestimo import deletar_emprestimo

def listar_emprestimos():
    emprestimos = buscar_emprestimos()
    return jsonify(emprestimos)

def listar_emprestimo_por_id(emprestimo_id):
    emprestimo = buscar_emprestimo_por_id(emprestimo_id)
    if not emprestimo:
        return jsonify({"erro": "Emprestimo não encontrado"}), 404
    return jsonify(emprestimo), 200

def criar_emprestimo():
    data = request.get_json()
    emprestimo = cadastrar_emprestimo(data)
    if "erro" in emprestimo:
        return jsonify(emprestimo), 409
    return jsonify(emprestimo), 201

def editar_emprestimo(emprestimo_id):
    data = request.get_json()
    emprestimo = atualizar_emprestimo(emprestimo_id, data)
    if not emprestimo:
        return jsonify({"erro": "Emprestimo não encontrado"}), 404
    return jsonify(emprestimo), 200

def remover_emprestimo(emprestimo_id):
    removido = deletar_emprestimo(emprestimo_id)
    if "erro" in removido:
        if removido["erro"] == "Emprestimo não encontrado":
            return jsonify(removido), 404
        return jsonify(removido), 409
    return jsonify(removido), 200