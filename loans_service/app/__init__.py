from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Registra APENAS o blueprint de empréstimos
    from app.routes.emprestimo_routes import emprestimo_bp
    app.register_blueprint(emprestimo_bp)

    return app