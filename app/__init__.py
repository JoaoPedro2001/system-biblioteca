from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    CORS(app)

    from app.routes.livro_routes import livro_bp

    app.register_blueprint(livro_bp)

    return app