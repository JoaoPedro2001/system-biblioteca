from flask import Blueprint
from app.controllers.bibliotecario_controller import(
    listar_bibliotecarios,
    listar_bibliotecario_por_id,
    criar_bibliotecario,
    editar_bibliotecario,
    remover_bibliotecario
)

bibliotecario_bp = Blueprint("bibliotecarios", __name__)

bibliotecario_bp.route("/bibliotecarios", methods=["GET"])(listar_bibliotecarios)
bibliotecario_bp.route("/bibliotecarios/<int:bibliotecario_id>", methods=["GET"])(listar_bibliotecario_por_id)
bibliotecario_bp.route("/bibliotecarios", methods=["POST"])(criar_bibliotecario)
bibliotecario_bp.route("/bibliotecarios/<int:bibliotecario_id>", methods=["PUT"])(editar_bibliotecario)
bibliotecario_bp.route("/bibliotecarios/<int:bibliotecario_id>", methods=["DELETE"])(remover_bibliotecario)