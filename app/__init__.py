from flask import Flask
from .models import db
from app.config import BASE_DIR

def create_app():
    app = Flask(__name__)

    # Configurações
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar banco
    db.init_app(app)

    with app.app_context():
        db.create_all()

        # Importar rotas
        from app import rotas

        # Registrar API
        from .api import api_bp
        app.register_blueprint(api_bp, url_prefix="/api")

        # Inicializar servidores/processos salvos
        from app.api_server.manager import load_servers_from_db
        load_servers_from_db()

    return app
