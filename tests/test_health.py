import requests

def test_health_api_check():
    response = requests.get("https://fakestoreapi.com/products")
    assert response.status_code == 200
