import requests

def test_login_success():
    """Se busca validar el login exitoso con credenciales correctas"""
    url = "https://fakestoreapi.com/auth/login"
    payload = {
        "username": "johnd",
        "password": "m38rmF$"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 201
    data = response.json()
    assert "token" in data
    assert isinstance(data["token"], str)

def test_login_with_wrong_password():
    """Se valida el manejo de login con contraseña incorrecta"""
    url = "https://fakestoreapi.com/auth/login"
    payload = {
        "username": "johnd",
        "password": "wrongpassword"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 401