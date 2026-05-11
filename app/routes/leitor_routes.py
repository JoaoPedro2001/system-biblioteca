from flask import Blueprint
from app.controllers.leitor_controller import(
    listar_leitores,
    listar_leitor_por_id,
    criar_leitor,
    editar_leitor,
    remover_leitor
)

leitor_bp = Blueprint("leitores", __name__)

leitor_bp.route("/leitores", methods=["GET"])(listar_leitores)
leitor_bp.route("/leitores/<int:leitor_id>", methods=["GET"])(listar_leitor_por_id)
leitor_bp.route("/leitores", methods=["POST"])(criar_leitor)
leitor_bp.route("/leitores/<int:leitor_id>", methods=["PUT"])(editar_leitor)
leitor_bp.route("/leitores/<int:leitor_id>", methods=["DELETE"])(remover_leitor)