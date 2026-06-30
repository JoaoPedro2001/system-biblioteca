import os
from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Registra APENAS o blueprint de autenticação/bibliotecários
    from app.routes.bibliotecario_routes import bibliotecario_bp
    app.register_blueprint(bibliotecario_bp)

    return app