from flask import Flask, send_from_directory
from flask_cors import CORS

from pathlib import Path

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

    # Caminho absoluto da pasta views
    BASE_DIR = Path(__file__).resolve().parent

    VIEWS_DIR = BASE_DIR / "views"

    PAGES_DIR = VIEWS_DIR / "pages"

    JS_DIR = VIEWS_DIR / "js"

    # Página inicial
    @app.route("/")
    def home():

        return send_from_directory(
            VIEWS_DIR,
            "index.html"
        )

    # Páginas HTML
    @app.route("/pages/<path:nome_arquivo>")
    def paginas(nome_arquivo):

        return send_from_directory(
            PAGES_DIR,
            nome_arquivo
        )

    # Arquivos JS
    @app.route("/js/<path:nome_arquivo>")
    def javascript(nome_arquivo):

        return send_from_directory(
            JS_DIR,
            nome_arquivo
        )

    return app