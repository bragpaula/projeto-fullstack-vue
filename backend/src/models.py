from utils import db
from datetime import datetime

class Usuario(db.Model): 
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True, name='email')
    senha = db.Column(db.String(100), nullable=False)

    def __init__(self, nome, email, senha): # is admin false como padrão, pois se o valor não for passado, o usuário não 
        self.nome = nome
        self.email = email
        self.senha = senha
        
class Mensagem(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    titulo = db.Column(db.String(45), nullable = False)
    conteudo = db.Column(db.String(200), nullable = False)
    autor = db.Column(db.String(45), nullable = False)
    created_at = db.Column(db.DateTime(), default=datetime.now)
    usuario = db.relationship('Usuario',foreign_keys=usuario_id)
    comentarios = db.relationship('Comentario', back_populates='mensagem')
    
    def __init__(self, titulo, conteudo, autor, usuario_id):
        self.titulo = titulo
        self.conteudo = conteudo
        self.autor = autor
        self.usuario_id = usuario_id

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "conteudo": self.conteudo,
            "autor": self.autor,
            "usuario_id": self.usuario_id,
            "created_at": self.created_at.isoformat()
        }



class Comentario(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    mensagem_id = db.Column(db.Integer, db.ForeignKey('mensagem.id'))
    conteudo = db.Column(db.String(200), nullable = False)
    autor = db.Column(db.String(45), nullable = False)
    created_at = db.Column(db.DateTime(), default=datetime.now)
    mensagem = db.relationship('Mensagem', foreign_keys=mensagem_id, back_populates='comentarios')

    def __init__(self, mensagem_id, conteudo, autor):
        self.mensagem_id = mensagem_id
        self.conteudo = conteudo
        self.autor = autor

    def to_dict(self):
        return {
            "id": self.id,
            "conteudo": self.conteudo, 
            "autor": self.autor,
            "mensagem_id": self.mensagem_id,
            "data_criacao": self.created_at.isoformat() if self.created_at else None
        }
    
    
    