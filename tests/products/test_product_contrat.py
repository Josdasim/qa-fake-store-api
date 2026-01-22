from core.api_client import ApiClient


def test_product_structure(api_client: ApiClient):
    """Se valida la estructura del primer producto obtenido"""
    response = api_client.get("/products")
    products = response.json()

    first_product = products[0]

    assert "id" in first_product
    assert "title" in first_product
    assert "price" in first_product
    assert "description" in first_product
    assert "category" in first_product
    assert "image" in first_product
    assert "rating" in first_product

def test_product_fields_types(api_client: ApiClient):
    """Se valida que los tipos de datos de los campos del producto sean correctos"""
    response = api_client.get("/products")
    product = response.json()[0]

    assert isinstance(product["id"], int)
    assert isinstance(product["title"], str)
    assert isinstance(product["price"], (int, float))
    assert isinstance(product["description"], str)
    assert isinstance(product["category"], str)
    assert isinstance(product["image"], str)