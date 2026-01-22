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

def test_validate_product_fields(api_client: ApiClient):
    """Se valida que cada producto contenga la estructura correcta"""
    response = api_client.get("/products")
    products = response.json()

    expected_keys = {"id", "title", "price", "description", "category", "image", "rating"}

    for product in products:
        assert set(product.keys()) == expected_keys

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