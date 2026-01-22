# QA Automation - Fake Store API

## Descripcion General
Este proyecto contiene un conjunto de pruebas automatizadas para la API de 'Fake Store' ("https://fakestoreapi.com/").

El objetivo es validar las funcionalidades principales y el manejo de errores usando python y pytest.

## Test Plan

### Alcance de las pruebas
- Autenticacion de usuarios (login)
- Productos
- Disponibilidad basica de la API

### Tipos de pruebas
- Pruebas de funcionalidad
- Pruebas negativas

### Fuera del alcance
- Pruebas de rendimiento
- Pruebas de seguridad
- Pruebas de Interfaz de Usuario (UI)

### Entorno de pruebas
- API Endpoint: https://fakestoreapi.com/
- Herramientas: Python, pytest, requests

### Criterios de entrada
- Que la API de Fake Store este operativa
- Que las herramientas de prueba esten configuradas correctamente

### Criterios de salida
- Todas las pruebas automatizadas se ejecutan con exito
- No hay errores criticos en las funcionalidades probadas

### Riesgos
- Inestabilidad o tiempo de inactividad de la API durante las pruebas
- Cambios inesperados en la API que puedan romper las pruebas
- Problemas de conectividad de red durante la ejecucion de las pruebas
