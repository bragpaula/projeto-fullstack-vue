from flask import Blueprint, request, jsonify
from utils import db
from models import Usuario
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

usuario_bp = Blueprint('usuario_bp', __name__, url_prefix='/auth')


@usuario_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    username = data['nome']
    email = data['email']
    password = data['senha']
    hashedPassword = generate_password_hash(password)
    existentEmail =  Usuario.query.filter_by(email=email).first()

    if existentEmail:
        return jsonify({"error": "email already exists"}), 409
    
    newUser = Usuario(username, email, hashedPassword)
    db.session.add(newUser)
    db.session.commit()

    token = create_access_token(identity=str(newUser.id))

    return jsonify({'accessToken': token, 'user': {
            "nome":newUser.nome,
            "email":newUser.email
        }}), 201


@usuario_bp.route('/login', methods=['POST'])
def login():

    data = request.get_json()

    email = data['email']
    password = data['senha']

    user = Usuario.query.filter_by(email=email).first()
    if user is None:
        return jsonify({'error': 'email or password incorrect'}), 401
    
    token = create_access_token(identity=str(user.id))

    if user is not None and check_password_hash(user.senha, password):
        return jsonify({'accessToken': token, 'user': {
            "nome":user.nome,
            "email":user.email
        }}), 200

    return jsonify({"error": "email or password incorrect"}), 401