from flask import Blueprint
from app.controllers.emprestimo_controller import(
    listar_emprestimos,
    listar_emprestimo_por_id,
    criar_emprestimo,
    editar_emprestimo,
    remover_emprestimo
)

emprestimo_bp = Blueprint("emprestimos", __name__)

emprestimo_bp.route("/emprestimos", methods=["GET"])(listar_emprestimos)
emprestimo_bp.route("/emprestimos/<int:emprestimo_id>", methods=["GET"])(listar_emprestimo_por_id)
emprestimo_bp.route("/emprestimos", methods=["POST"])(criar_emprestimo)
emprestimo_bp.route("/emprestimos/<int:emprestimo_id>", methods=["PUT"])(editar_emprestimo)
emprestimo_bp.route("/emprestimos/<int:emprestimo_id>", methods=["DELETE"])(remover_emprestimo)