from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Registra os blueprints pertinentes ao catálogo do sistema
    from app.routes.livro_routes import livro_bp
    from app.routes.leitor_routes import leitor_bp

    app.register_blueprint(livro_bp)
    app.register_blueprint(leitor_bp)

    return app