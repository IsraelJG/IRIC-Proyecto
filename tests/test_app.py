# tests/test_app.py

# Importamos la instancia de la aplicación Flask que creaste
from app import app 

# pytest detectará automáticamente cualquier función que empiece con 'test_'

def test_home_page_status():
    """Prueba que la página principal responde con éxito (código 200)."""
    # Usamos el cliente de prueba de Flask para simular una solicitud HTTP
    with app.test_client() as client:
        response = client.get('/')
        # Verificamos que el código de estado es 200 (OK)
        assert response.status_code == 200
        # Opcional: Podrías verificar si el contenido contiene tu nombre
        assert b'Marvin Israel Jaramillo Garcia' in response.data

def test_health_check_status():
    """Prueba que la ruta /health responde correctamente con status: ok."""
    with app.test_client() as client:
        response = client.get('/health')
        # Verificamos que el código de estado es 200 (OK)
        assert response.status_code == 200
        # Verificamos que el JSON devuelto es {"status": "ok"}
        assert response.get_json() == {"status": "ok"}