from flask import Flask, render_template, url_for, request, flash, session
from flask_migrate import Migrate
from werkzeug.utils import redirect
from models import Usuario
from models import UpMedia
from models import Post
from database import db
from forms import UsuarioForm
from PIL import Image
import io
import base64
import psycopg2
import psycopg2.extras
import re


app = Flask(__name__)

USER_DB = "postgres"
PASS_DB = "Estudio8"
URL_DB = "localhost"
NAME_DB = "fallout4"
FULL_URL_DB = f"postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}"

app.config["SQLALCHEMY_DATABASE_URI"] = FULL_URL_DB
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)

migrate = Migrate()
migrate.init_app(app, db)

app.config["SECRET_KEY"] = "s*02_325/-/+6/-.SS,23"


@app.route("/imagenes")
def image():
    bytea_enc =Post.query.filter_by(titulo= "prueba2").first()
    imagenCod = bytea_enc.image
    
    imagen = Image.open(imagenCod)
    data = io.BytesIO()
    imagen.save(data, "JPEG")

    encode_img_data = base64.b64encode(data.getvalue()).decode("utf-8")
  
    return render_template('index.html', imagenUsar=encode_img_data)



@app.route("/")
def inicio():
    if 'Usuario' in session:
        name = session['Usuario']
        post = Post.query.all()
        return render_template("home.html", nameUser = name, posts=post)
    else:
        return render_template("indexNologin.html")


@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        usuario = request.form["Usuario"]
        contraseña = request.form["Contraseña"]

        # Consultar el usuario en la base de datos
        user = Usuario.query.filter_by(name=usuario).first()

        if user and user.password == contraseña:
            session['Usuario'] = usuario
            return redirect(url_for('inicio'))
        else:
            return render_template('login-fallido.html')
    return render_template('login.html')


@app.route("/logout")
def logout():
    session.pop('Usuario')
    return redirect(url_for('inicio'))


@app.route("/register", methods=["GET", "POST"])
def register():
    usuario = Usuario()
    usuarioForm = UsuarioForm(obj=usuario)

    if request.method == "POST":
        if usuarioForm.validate_on_submit():
            usuarioForm.populate_obj(usuario)
            app.logger.debug('persona a insertar:', usuario)
            db.session.add(usuario)
            db.session.commit()
            return redirect(url_for('login'))
    return render_template("register.html", forma = usuarioForm)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


    




# @app.route("/", methods=["GET", "POST"])
# def index():
#     if request.method == "POST":
#         file = request.files['file']
#         upload = UpMedia(filename=file.filename, data=file.read())
#         print(file.filename)
#         db.session.add(upload)
#         db.session.commit()
#         return ("Imagen Guardada con Exito")
#     return render_template('index.html')

# @app.route("/imagenes")
# def mostrar_imagen():
#     imagen = UpMedia.query.all()

#     return render_template('ver.html', imagenes=imagen)

# @app.route("/")
# def inicio():
#     personas = Persona.query.order_by(Persona.id).all()
#     total_personas = Persona.query.count()
#     return render_template(
#         "personas.html", personas=personas, total_personas=total_personas
#     )


# @app.route("/ver/<int:id>")
# def ver_detalle(id):
#     persona = Persona.query.get_or_404(id)
#     return render_template("detalle.html", persona=persona)


# @app.route("/agregar", methods=["GET", "POST"])
# def agregar():
#     persona = Persona()
#     personaForm = PersonaForm(obj=persona)

#     if request.method == "POST":
#         if personaForm.validate_on_submit():
#             personaForm.populate_obj(persona)
#             db.session.add(persona)
#             db.session.commit()
#             return redirect(url_for("inicio"))
#     return render_template("agregar.html", forma=personaForm)


# @app.route("/editar/<int:id>", methods=["GET", "POST"])
# def editar(id):
#     persona = Persona.query.get_or_404(id)
#     personaForma = PersonaForm(obj=persona)
#     if request.method == "POST":
#         if personaForma.validate_on_submit():
#             personaForma.populate_obj(persona)
#             db.session.commit()
#             return redirect(url_for("inicio"))
#     return render_template("editar.html", forma=personaForma)

# @app.route('/eliminar/<int:id>')
# def eliminar(id):
#     persona = Persona.query.get_or_404(id)
#     db.session.delete(persona)
#     db.session.commit()
#     return redirect(url_for('inicio'))

if __name__ == "__main__":
    app.run(debug=True)
