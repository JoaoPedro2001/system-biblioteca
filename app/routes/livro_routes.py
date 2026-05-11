from flask import Blueprint
from app.controllers.livro_controller import (
    listar_livros,
    criar_livro,
    listar_livro_por_id,
    editar_livro,
    remover_livro
    )

livro_bp = Blueprint("livros", __name__)

livro_bp.route("/livros", methods=["GET"])(listar_livros)
livro_bp.route("/livros/<int:livro_id>",methods=["GET"])(listar_livro_por_id)
livro_bp.route("/livros", methods=["POST"])(criar_livro)
livro_bp.route("/livros/<int:livro_id>", methods=["PUT"])(editar_livro)
livro_bp.route("/livros/<int:livro_id>", methods=["DELETE"])(remover_livro)