from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class UsuarioForm(FlaskForm):
    name = StringField("Nombre", validators=[DataRequired()], render_kw={'class':' form-control', 'placeholder':'Nombre'})
    password = StringField("Contraseña", validators=[DataRequired()], render_kw={'class':' form-control', 'placeholder':'Contraseña', "type":"password"})
    nick = StringField("Apellido", render_kw={'class':'form-control', 'placeholder':'Nick'})
    email = StringField("Email", validators=[DataRequired()], render_kw={'class':'form-control', 'placeholder':'Email@example.com'})
    enviar = SubmitField("Registrar", render_kw={'class':" btn btn-lg btn-primary my-3 w-50 h-50"})
