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

2. **BUG-002: API externa bloqueada en GitHub Actions**

    **Endpoint:** Todos los endpoints (por ejemplo, `/auth/login`)

    **Descripcion:** Fake Store API parece estar bloqueada o inaccesible(posiblemente por cloudflare) desde el entorno de GitHub Actions, lo que impide la ejecucion de pruebas automatizadas en este entorno CI.

    **Pasos para reproducir:**
    - Ejecutar el pipeline de GitHub Actions que incluye pruebas contra la API de Fake Store

    **Resultado esperado:**
    - Todas las pruebas se ejecutan correctamente y la API responde como se espera.

    **Resultado actual:**
    - Las solicitudes a la API fallan debido a problemas de conectividad o bloqueos, haciendo que las pruebas fallen al comparar codigos de estado esperados.

    **Impacto:** 
    - Imposibilita la ejecucion de pruebas automatizadas en el entorno CI.

    **Evidencia:**
    - Logs del pipeline de GitHub Actions mostrando errores de conexion al intentar acceder a la API.

    **Severidad:** 
    - Media

    **Estado:** 
    - Abierto

    ## Notas Adicionales

    **Causas Potenciales:**
    - La API de Fake Store puede tener restricciones de acceso desde ciertos entornos o IPs (No encontrado en la documentacion oficial)
    - Bloqueo por parte de servicios de seguridad como Cloudflare (hipotetico, con base a las respuesta dadas en las lineas 92, 211, 330...)