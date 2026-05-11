from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    CORS(app)

    from app.routes.livro_routes import livro_bp
    from app.routes.leitor_routes import leitor_bp
    from app.routes.bibliotecario_routes import bibliotecario_bp
    from app.routes.emprestimo_routes import emprestimo_bp

    app.register_blueprint(livro_bp)
    app.register_blueprint(leitor_bp)
    app.register_blueprint(bibliotecario_bp)
    app.register_blueprint(emprestimo_bp)

    return app