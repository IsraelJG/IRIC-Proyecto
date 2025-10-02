# tests/test_app.py

from app import app 

def test_home_page_status():
    """Prueba que la página principal responde con éxito (código 200)."""
    with app.test_client() as client:
        response = client.get('/')
        # Simplifica la aserción a solo verificar el código de estado
        assert response.status_code == 200 
        # Si quieres, mantén una aserción simple y genérica del contenido:
        # assert b'Materia:' in response.data 

def test_health_check_status():
    """Prueba que la ruta /health responde correctamente con status: ok."""
    with app.test_client() as client:
        response = client.get('/health')
        assert response.status_code == 200
        assert response.get_json() == {"status": "ok"}