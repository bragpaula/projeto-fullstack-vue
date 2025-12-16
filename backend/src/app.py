from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from utils import db
from models import Mensagem, Comentario, Usuario
from routes.usuario import usuario_bp
from routes.mensagem import mensagens_bp
from routes.comentario import comentarios_bp
from dotenv import load_dotenv
from flask_cors import CORS
import os

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

    # Configuração CORS - DEVE vir ANTES de registrar blueprints
    CORS(app, 
         origins=["http://localhost:5173"],
         methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
         allow_headers=["Content-Type", "Authorization"],
         supports_credentials=True,
         automatic_options=True)

    db.init_app(app)
    Migrate(app, db)
    JWTManager(app)

    # Handler manual para OPTIONS (preflight) - garante que funcione
    @app.before_request
    def handle_preflight():
        if request.method == "OPTIONS":
            response = jsonify({})
            response.headers.add("Access-Control-Allow-Origin", "http://localhost:5173")
            response.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")
            response.headers.add("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
            response.headers.add("Access-Control-Allow-Credentials", "true")
            return response

    app.register_blueprint(usuario_bp)
    app.register_blueprint(mensagens_bp)
    app.register_blueprint(comentarios_bp)

    return app

app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
