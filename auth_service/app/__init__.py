import os
from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    from app.routes.bibliotecario_routes import bibliotecario_bp
    from app.routes.autenticar_routes import autenticar_bp

    app.register_blueprint(bibliotecario_bp)
    app.register_blueprint(autenticar_bp)

    return app