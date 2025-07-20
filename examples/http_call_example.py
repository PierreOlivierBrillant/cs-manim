"""
Exemple d'utilisation de la classe HttpCall
"""

from manim import Scene, Create, FadeIn, UP, DOWN

from cs_manim import HttpCall


class HttpCallExample(Scene):
    def construct(self):
        # Exemple 1: Requête GET simple
        get_request = HttpCall(
            method="GET",
            url="/api/users/123",
            http_version="HTTP/1.1",
            headers={
                "Accept": "application/json",
                "Authorization": "Bearer token123",
                "User-Agent": "MyApp/1.0"
            }
        )
        get_request.scale(0.7)
        get_request.shift(UP * 2)

        # Exemple 2: Requête POST avec corps JSON
        post_request = HttpCall(
            method="POST",
            url="/api/users",
            http_version="HTTP/1.1",
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Authorization": "Bearer token123"
            },
            body='{"name": "John Doe", "email": "john@example.com", "age": 30}',
            body_language="json"
        )
        post_request.scale(0.6)
        post_request.shift(DOWN * 1)

        # Animation
        self.play(Create(get_request))
        self.wait(1)
        self.play(FadeIn(post_request))
        self.wait(3)


if __name__ == "__main__":
    # Pour exécuter cette scène, utilisez :
    # manim examples/http_call_example.py HttpCallExample
    pass
