# Known Issues

Este documento recopila los comportamientos incorrectos o inesperados detectados durante las pruebas de la API de Fake Store

## Problemas Identificados

1. **BUG-001: ID invalido en productos, retorna codigo 200 con cuerpo vacio**

    **Endpoint:** `/products/{id}`

    **Descripcion:** Al solicitar un producto con un ID que no existe (por ejemplo, nonexistent_id), la API retorna un codigo de estado 200 pero con un cuerpo vacio en lugar de un error 404 o un mensaje de error adecuado.

    **Pasos para reproducir:**
    - Realizar una solicitud GET a `/products/nonexistent_id`

    **Resultado esperado:**
    - Codigo 400 Bad Request o 404 Not Found 
    - Mensaje de error indicando que el producto no existe en formato JSON

    **Resultado actual:**
    - Codigo 200 OK
    - Cuerpo vacio
    - No devuelve JSON valido

    **Impacto:** 
    - Puede llevar a confusiones en los clientes de la API que esperan un manejo adecuado de errores.

    **Evidencia:**
    - Test automatizado `test_get_product_with_invalid_id` en `tests/test_products.py` que valida este comportamiento incorrecto.

    **Severidad:** 
    - Media

    **Estado:** 
    - Abierto

