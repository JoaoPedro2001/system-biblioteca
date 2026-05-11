from flask import Blueprint
from app.controllers.livro_controller import (
    listar_livros,
    criar_livro
    )

livro_bp = Blueprint("livros", __name__)

livro_bp.route("/livros", methods=["GET"])(listar_livros)
livro_bp.route("/livros", methods=["POST"])(criar_livro)