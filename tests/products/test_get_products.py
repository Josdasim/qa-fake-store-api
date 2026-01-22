from core.api_client import ApiClient


def test_health_endpont_products(api_client: ApiClient):
    """Se valida una respuesta positiva del endpoint de productos"""
    response = api_client.get("/products")
    assert response.status_code == 200

def test_get_all_products(api_client: ApiClient):
    """Se valida la obtencion de todos los productos correctamente"""
    response = api_client.get("/products")
    products = response.json()

    assert isinstance(products, list)
    assert len(products) > 0