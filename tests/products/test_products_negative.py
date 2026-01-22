from core.api_client import ApiClient


def test_product_invalid_endpoint(api_client: ApiClient):
    """Se valida que un endpoint invalido retorna un 404"""
    response = api_client.get("/productsx")
    assert response.status_code == 404


def test_product_with_invalid_id(api_client: ApiClient):
    """Este test es valido para verificar el comportamiento al solicitar un ID de producto no existente, en este caso se busca ver que retorna un 200 con cuerpo vacio"""
    response = api_client.get("/products/nonexistent_id")
    assert response.status_code == 200
    assert response.text == ""
    # Se deberia registrar como un bug, ya que la API deberia retornar un 404 Not Found, al intentar buscar un producto con un ID no existente
