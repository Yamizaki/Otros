from database import db
from datetime import datetime
from PIL import Image

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    nick = db.Column(db.String(250))
    password = db.Column(db.String(250))
    email = db.Column(db.String(250))

    def __str__(self):
        return (
            f"Id: {self.id}, "
            f"Nombre: {self.name}, "
            f"Apellido: {self.nick}, "
            f"Email: {self.email}"
        )
class UpMedia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(50))
    data = db.Column(db.LargeBinary)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50))
    image = db.Column(db.LargeBinary)
    info = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)