"""Test pour la classe HttpCall mise à jour."""

from cs_manim.objects.http_call import HttpCall


def test_http_call_creation():
    """Test que HttpCall peut être créé avec les paramètres par défaut."""
    http_call = HttpCall()
    assert http_call is not None


def test_http_call_with_custom_params():
    """Test que HttpCall peut être créé avec des paramètres personnalisés."""
    http_call = HttpCall(
        method="POST",
        url="/api/users",
        http_version="HTTP/2.0",
        headers={"Content-Type": "application/json"},
        body='{"name": "test"}',
        body_language="json",
    )
    assert http_call is not None


def test_http_call_method_colors():
    """Test que les couleurs des méthodes HTTP sont correctement assignées."""
    http_call = HttpCall()

    # Tester différentes méthodes
    assert http_call._get_method_color("GET") is not None
    assert http_call._get_method_color("POST") is not None
    assert http_call._get_method_color("PUT") is not None
    assert http_call._get_method_color("DELETE") is not None
    assert (
        http_call._get_method_color("UNKNOWN") is not None
    )  # Devrait retourner REQUEST_COLOR


def test_http_call_with_json_body():
    """Test HttpCall avec un corps JSON valide."""
    json_body = '{"name": "John", "email": "john@example.com"}'
    http_call = HttpCall(
        method="POST", url="/api/users", body=json_body, body_language="json"
    )
    assert http_call is not None


def test_http_call_with_invalid_json():
    """Test HttpCall avec un JSON invalide (devrait gérer l'erreur)."""
    invalid_json = '{"name": "John", "email": invalid}'
    http_call = HttpCall(
        method="POST", url="/api/users", body=invalid_json, body_language="json"
    )
    assert http_call is not None  # Ne devrait pas lever d'exception


def test_http_call_with_headers():
    """Test HttpCall avec des en-têtes."""
    headers = {
        "Authorization": "Bearer token123",
        "Content-Type": "application/json",
        "User-Agent": "TestAgent/1.0",
    }
    http_call = HttpCall(method="GET", url="/api/data", headers=headers)
    assert http_call is not None
