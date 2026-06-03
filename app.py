from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", 
                                                  "postgresql://miranda_api_db_user:1yLS5e6We92Lz3JZ6AUG2Fhfu0kc98LC@dpg-d8eoqmsp3tds738qbks0-a.oregon-postgres.render.com/miranda_api_db"
                                                  )
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()


class Cliente(db.Model):
    __tablename__ = "clientes"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(50))


def cliente_a_diccionario(cliente):
    return {
        "id": cliente.id,
        "nombre": cliente.nombre,
        "apellido": cliente.apellido,
        "email": cliente.email,
        "telefono": cliente.telefono
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/clientes", methods=["GET"])
def obtener_clientes():

    clientes = Cliente.query.all()

    return jsonify(
        [cliente_a_diccionario(cliente) for cliente in clientes]
    )


@app.route("/clientes/<int:id_cliente>", methods=["GET"])
def obtener_cliente(id_cliente):

    cliente = Cliente.query.get(id_cliente)

    if cliente is None:
        return jsonify({"error": "Cliente no encontrado"}), 404

    return jsonify(cliente_a_diccionario(cliente))


@app.route("/clientes", methods=["POST"])
def crear_cliente():

    data = request.get_json()

    if not data:
        return jsonify({"error": "Datos inválidos"}), 400

    nombre = data.get("nombre")
    apellido = data.get("apellido")
    email = data.get("email")
    telefono = data.get("telefono")

    if not nombre or not apellido or not email:
        return jsonify(
            {"error": "Nombre, apellido y email son obligatorios"}
        ), 400

    cliente = Cliente(
        nombre=nombre,
        apellido=apellido,
        email=email,
        telefono=telefono
    )

    db.session.add(cliente)
    db.session.commit()

    return jsonify(cliente_a_diccionario(cliente)), 201


@app.route("/clientes/<int:id_cliente>", methods=["PUT"])
def actualizar_cliente(id_cliente):

    cliente = Cliente.query.get(id_cliente)

    if cliente is None:
        return jsonify({"error": "Cliente no encontrado"}), 404

    data = request.get_json()

    if not data:
        return jsonify({"error": "Datos inválidos"}), 400

    cliente.nombre = data.get("nombre", cliente.nombre)
    cliente.apellido = data.get("apellido", cliente.apellido)
    cliente.email = data.get("email", cliente.email)
    cliente.telefono = data.get("telefono", cliente.telefono)

    db.session.commit()

    return jsonify(cliente_a_diccionario(cliente))


@app.route("/clientes/<int:id_cliente>", methods=["DELETE"])
def eliminar_cliente(id_cliente):

    cliente = Cliente.query.get(id_cliente)

    if cliente is None:
        return jsonify({"error": "Cliente no encontrado"}), 404

    db.session.delete(cliente)
    db.session.commit()

    return jsonify({"mensaje": "Cliente eliminado"})


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=port)