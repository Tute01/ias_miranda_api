import pytest
from app import app


@pytest.mark.integration
def test_get_clientes():

    client = app.test_client()

    response = client.get("/clientes")

    assert response.status_code == 200


@pytest.mark.integration
def test_crear_cliente():

    client = app.test_client()

    data = {
        "nombre": "Juan",
        "apellido": "Perez",
        "email": "juan@test.com",
        "telefono": "1122334455"
    }

    response = client.post(
        "/clientes",
        json=data
    )

    assert response.status_code == 201

    body = response.get_json()

    assert body["nombre"] == "Juan"
    assert body["apellido"] == "Perez"


@pytest.mark.integration
def test_obtener_cliente():

    client = app.test_client()

    data = {
        "nombre": "Pedro",
        "apellido": "Gomez",
        "email": "pedro@test.com"
    }

    crear = client.post(
        "/clientes",
        json=data
    )

    cliente = crear.get_json()

    response = client.get(
        f"/clientes/{cliente['id']}"
    )

    assert response.status_code == 200

    body = response.get_json()

    assert body["id"] == cliente["id"]