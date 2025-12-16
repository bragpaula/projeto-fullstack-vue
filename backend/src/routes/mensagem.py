from flask import Blueprint, request, jsonify
from models import Mensagem, Usuario
from utils import db
from flask_jwt_extended import jwt_required, get_jwt_identity

mensagens_bp = Blueprint('mensagens_bp', __name__, url_prefix='/mensagens')

# Aceita /mensagens e /mensagens/ sem redirecionar (evita 308 no preflight)
@mensagens_bp.route('', methods=['GET'])
@mensagens_bp.route('/', methods=['GET'])
def get_messages():
    mensagens = Mensagem.query.all()
    mensagens = [mensagem.to_dict() for mensagem in mensagens]
    return jsonify(mensagens), 200

@mensagens_bp.route('/<int:message_id>', methods=['GET'])
def get_message(message_id):
    mensagem = Mensagem.query.filter_by(id=message_id).first()
    if mensagem:
        return jsonify(mensagem.to_dict()), 200
    return jsonify({"error":"mensagem inexistente!"}), 400

    

@mensagens_bp.route('', methods=['POST'])
@mensagens_bp.route('/', methods=['POST'])
@jwt_required()
def create_message():
    user_id = get_jwt_identity()
    usuario = Usuario.query.filter_by(id=user_id).first()
    data = request.get_json()
    novaMensagem = Mensagem(data['titulo'], data['conteudo'], usuario.nome, user_id)
    db.session.add(novaMensagem)
    db.session.commit()
    return jsonify(novaMensagem.to_dict()), 201


@mensagens_bp.route('/<int:message_id>', methods=['PUT'])
@jwt_required()
def update_message(message_id):
    user_id = get_jwt_identity()
    data = request.get_json()
    mensagem = Mensagem.query.filter_by(id=message_id).first()
    if mensagem.usuario_id != int(user_id):
        return jsonify({"error": "Acesso negado."}), 403

    mensagem.titulo = data["titulo"]
    mensagem.conteudo = data["conteudo"]
    db.session.commit()
    return jsonify(mensagem.to_dict()), 200



@mensagens_bp.route('/<int:message_id>', methods=['DELETE'])
@jwt_required()
def delete_message(message_id):
    mensagem = Mensagem.query.get_or_404(message_id)
    print(type(mensagem.usuario_id))
    print(type(get_jwt_identity()))

    if mensagem.usuario_id != int(get_jwt_identity()):
        return jsonify({"error": "Acesso negado."}), 403
    db.session.delete(mensagem)
    db.session.commit()
    return '', 204