from flask import Blueprint, request, jsonify
from models import Comentario, Mensagem, Usuario
from utils import db
from flask_jwt_extended import jwt_required, get_jwt_identity

comentarios_bp = Blueprint('comentarios_bp', __name__, url_prefix='/mensagens')

@comentarios_bp.route('/<int:id>/comentarios', methods=['GET'])
@jwt_required()
def get_comments(id):
    mensagem = Mensagem.query.filter_by(id=id).first()
    comentarios = [comentario.to_dict() for comentario in mensagem.comentarios]
    return jsonify(comentarios), 200


@comentarios_bp.route('/<int:id>/comentarios', methods=['POST'])
@jwt_required()
def create_comment(id):
    mensagem_id = id
    user_id = get_jwt_identity()
    usuario = Usuario.query.filter_by(id=user_id).first()
    data = request.get_json()
    novoComentario = Comentario(mensagem_id, data['conteudo'], usuario.nome)
    db.session.add(novoComentario)
    db.session.commit()
    return jsonify(novoComentario.to_dict()), 201


@comentarios_bp.route('/comentarios/<int:comentario_id>', methods=['PUT'])
@jwt_required()
def update_comment(comentario_id):
    user_id = int(get_jwt_identity())
    comentario = Comentario.query.get_or_404(comentario_id)
    data = request.get_json()

    if comentario.mensagem.usuario_id != user_id:
        return jsonify({"error": "Acesso negado."}), 403

    comentario.conteudo = data['conteudo']
    db.session.commit()

    return jsonify(comentario.to_dict()), 200


@comentarios_bp.route('/comentarios/<int:comentario_id>', methods=['DELETE'])
@jwt_required()
def delete_comment(comentario_id):
    user_id = int(get_jwt_identity())
    comentario = Comentario.query.get_or_404(comentario_id)

    if comentario.mensagem.usuario_id != user_id:
        return jsonify({"error": "Acesso negado."}), 403

    db.session.delete(comentario)
    db.session.commit()

    return '', 204

