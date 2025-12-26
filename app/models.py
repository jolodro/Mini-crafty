from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Configuracao(db.Model):
    __tablename__ = "configuracoes"

    id = db.Column(db.Integer, primary_key=True)
    ftp_ativo = db.Column(db.Boolean, default=False)

class Servidor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(2000), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(20), nullable=False)
    versao = db.Column(db.String(20))

    ram = db.Column(db.Integer)
    porta = db.Column(db.Integer)
    status = db.Column(db.String(20), default="parado")
    pid = db.Column(db.Integer)
    start_time = db.Column(db.Float)

    def __repr__(self):
        return f"<Servidor {self.nome}>"

    def to_dict(self):
        return {
            "id": self.id,
            "path": self.path,
            "nome": self.nome,
            "tipo": self.tipo,
            "versao": self.versao,
            "ram": self.ram,
            "porta": self.porta,
            "status":self.status,
            "pid": self.pid,
            "start_time": self.start_time
        }