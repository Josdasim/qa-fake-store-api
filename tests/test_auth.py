from core.api_client import ApiClient

PATH = "/auth/login"

def test_login_success(api_client: ApiClient):
    """Se busca validar el login exitoso con credenciales correctas"""
    payload = {
        "username": "johnd",
        "password": "m38rmF$"
    }
    response = api_client.post(PATH, payload)
    assert response.status_code == 201
    data = response.json()
    assert "token" in data
    assert isinstance(data["token"], str)

def test_login_with_wrong_password(api_client: ApiClient):
    """Se valida el manejo de login con contraseña incorrecta"""
    payload = {
        "username": "johnd",
        "password": "wrongpassword"
    }
    response = api_client.post(PATH, payload)
    assert response.status_code == 401

def test_login_with_missing_fields(api_client: ApiClient):
    """Se valida el manejo de login con campos faltantes"""
    payload = {
        "username": "johnd"
        # Falta el campo 'password'
    }
    response = api_client.post(PATH, payload)
    assert response.status_code == 400  

def test_login_with_empty_payload(api_client: ApiClient):
    """Se valida el manejo de login con payload vacío"""
    payload = {}
    response = api_client.post(PATH, payload)
    assert response.status_code == 400

def test_login_with_blank_username(api_client: ApiClient):
    """Se valida el manejo de login con nombre de usuario en blanco"""
    payload = {
        "username": "",
        "password": "m38rmF$"
    }
    response = api_client.post(PATH, payload)
    assert response.status_code == 400

def test_login_with_blank_password(api_client: ApiClient):
    """Se valida el manejo de login con contraseña en blanco"""
    payload = {
        "username": "johnd",
        "password": ""
    }
    response = api_client.post(PATH, payload)
    assert response.status_code == 400

def test_login_with_space_only_password(api_client: ApiClient):
    """Se valida el manejo de login con contraseña que solo contiene espacios"""
    payload = {
        "username": "johnd",
        "password": " "
    }
    response = api_client.post(PATH, payload)
    assert response.status_code == 401