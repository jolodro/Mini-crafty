from flask import Flask
from .models import db
from app.config import BASE_DIR

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# Importar rotas e APIs
from app import rotas
from .api import api_bp

app.register_blueprint(api_bp, url_prefix="/api")

# Inicializar servidores ou processos existentes
from app.api_server.manager import load_servers_from_db
with app.app_context():
    load_servers_from_db()
