from flask import Blueprint

from app.controllers.autenticar_controller import login

autenticar_bp = Blueprint("autenticacao",__name__)

autenticar_bp.route("/login",methods=["POST"])(login)