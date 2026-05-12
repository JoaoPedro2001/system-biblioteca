from flask import jsonify, request
from app.services.emprestimo_service import(
    buscar_emprestimos,
    buscar_emprestimos_por_id,
    cadastrar_emprestimo,
    atualizar_emprestimo,
    deletar_emprestimos,
)

def listar_emprestimos():
    emprestimos = buscar_emprestimos()

    return jsonify(emprestimos)

def listar_emprestimo_por_id(emprestimo_id):
    emprestimo = buscar_emprestimos_por_id(emprestimo_id)

    if not emprestimo:
        return jsonify({
            "erro": "Emprestimo não encontrado"
        }), 404
    
    return jsonify(emprestimo), 200

def criar_emprestimo():
    data = request.get_json()

    emprestimo = cadastrar_emprestimo(data)

    return jsonify(emprestimo), 201

def editar_emprestimo(emprestimo_id):
    data = request.get_json()

    emprestimo = atualizar_emprestimo(emprestimo_id, data)

    if not emprestimo:
        return jsonify({
            "erro": "Emprestimo não encontrado"
        }), 404
    
    return jsonify(emprestimo), 200

def remover_emprestimo(emprestimo_id):
    removido = deletar_emprestimos(emprestimo_id)

    if not removido:
        return jsonify({
            "erro": "Emprestimo não encontrado"
        }), 404
    
    return jsonify({
        "mensagem": "Emprestimo removido com sucesso"
    }), 200