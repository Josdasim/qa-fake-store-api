import requests

def test_health_api_check():
    """Se busca validar la correcta respuesta de la api"""
    response = requests.get("https://fakestoreapi.com")
    assert response.status_code == 200

