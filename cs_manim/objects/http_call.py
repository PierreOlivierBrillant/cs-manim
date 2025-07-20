from typing import Dict, Optional

from manim import (
    BLUE,
    GREEN,
    LEFT,
    ORANGE,
    PURPLE,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Code,
    Rectangle,
    Text,
    VGroup,
)

from ..style import FONT_NAME, REQUEST_COLOR


class HttpCall(VGroup):
    def __init__(
        self,
        method: str = "GET",
        url: str = "/api/data",
        http_version: str = "HTTP/1.1",
        headers: Optional[Dict[str, str]] = None,
        body: Optional[str] = None,
        body_language: str = "json",
    ):
        """
        Créer une représentation textuelle d'un appel HTTP avec formatage et coloration

        Args:
            method: Méthode HTTP (default "GET")
            url: URL de l'appel (default "/api/data")
            http_version: Version HTTP (default "HTTP/1.1")
            headers: Dictionnaire des en-têtes HTTP (default None)
            body: Corps de la requête (default None)
            body_language: Langage pour la coloration syntaxique du corps (default "json")

        Returns:
            VGroup: Le groupe d'objets représentant l'appel HTTP
        """
        super().__init__()

        # Configuration des couleurs
        method_color = self._get_method_color(method)
        url_color = BLUE
        version_color = PURPLE
        header_key_color = GREEN
        header_value_color = WHITE
        border_color = WHITE
        background_color = "#1e1e1e"

        # Constantes de mise en page
        padding = 0.3
        line_height = 0.25
        font_size_header = 16
        font_size_body = 14

        # Container pour tous les éléments
        content_elements = []
        y_position = 0.0

        # 1. Ligne de requête principale (méthode, URL, version)
        method_text = Text(
            method, font=FONT_NAME, font_size=font_size_header, color=method_color
        )
        url_text = Text(
            url, font=FONT_NAME, font_size=font_size_header, color=url_color
        )
        version_text = Text(
            http_version,
            font=FONT_NAME,
            font_size=font_size_header,
            color=version_color,
        )

        request_line = VGroup(method_text, url_text, version_text).arrange(
            RIGHT, buff=0.2
        )
        request_line.align_to(LEFT * 3, LEFT)
        request_line.shift(UP * y_position)
        content_elements.append(request_line)
        y_position -= line_height

        # 2. En-têtes HTTP
        if headers:
            for key, value in headers.items():
                header_key = Text(
                    f"{key}:",
                    font=FONT_NAME,
                    font_size=font_size_header,
                    color=header_key_color,
                )
                header_value = Text(
                    value,
                    font=FONT_NAME,
                    font_size=font_size_header,
                    color=header_value_color,
                )

                header_line = VGroup(header_key, header_value).arrange(RIGHT, buff=0.15)
                header_line.align_to(LEFT * 3, LEFT)
                header_line.shift(UP * y_position)
                content_elements.append(header_line)
                y_position -= line_height

        # 3. Ligne vide entre en-têtes et corps
        if headers and body:
            y_position -= line_height * 0.5

        # 4. Corps de la requête
        if body:
            body_code = Code(
                code_string=body,
                formatter_style="emacs",
                background="rectangle",
                language=body_language,
                add_line_numbers=False,
                background_config={
                    "stroke_color": WHITE,
                    "fill_opacity": 0,
                    "buff": 0,
                    "stroke_width": 0,
                },
                paragraph_config={
                    "font": "Noto Sans Mono",
                    "font_size": font_size_body,
                },
            )
            y_position -= body_code.height / 2
            body_code.align_to(LEFT * 3, LEFT)
            body_code.shift(UP * y_position)
            content_elements.append(body_code)
            y_position -= line_height

        # Grouper tous les éléments de contenu
        if content_elements:
            content_group = VGroup(*content_elements)

            # Créer l'encadré avec padding
            border_width = content_group.width + 2 * padding
            border_height = content_group.height + 2 * padding

            border = Rectangle(
                width=border_width,
                height=border_height,
                stroke_color=border_color,
                stroke_width=2,
                fill_color=background_color,
                fill_opacity=0.1,
            )

            # Centrer le contenu dans l'encadré
            content_group.move_to(border.get_center())

            # Ajouter l'encadré et le contenu au VGroup principal
            self.add(border, content_group)
        else:
            # Fallback si aucun contenu
            fallback = Text("HTTP Request", font=FONT_NAME, color=WHITE)
            self.add(fallback)

    def _get_method_color(self, method: str):
        """
        Retourner une couleur appropriée selon la méthode HTTP

        Args:
            method: Méthode HTTP

        Returns:
            Couleur Manim correspondante
        """
        method_colors = {
            "GET": GREEN,
            "POST": BLUE,
            "PUT": ORANGE,
            "PATCH": YELLOW,
            "DELETE": RED,
            "HEAD": PURPLE,
            "OPTIONS": WHITE,
        }
        return method_colors.get(method.upper(), REQUEST_COLOR)

    def _get_json_line_color(self, line: str):
        """
        Retourner une couleur appropriée pour une ligne JSON

        Args:
            line: Ligne de JSON à colorer

        Returns:
            Couleur Manim correspondante
        """
        line = line.strip()

        # Accolades et crochets
        if line in ["{", "}", "[", "]"] or line.endswith("{") or line.endswith("["):
            return YELLOW

        # Clés JSON (contient des guillemets et deux points)
        if (
            '"' in line
            and ":" in line
            and not line.endswith(",")
            and not line.endswith("}")
        ):
            return GREEN

        # Valeurs string (commence par des espaces puis guillemets)
        if line.startswith('"') or ': "' in line:
            return BLUE

        # Valeurs numériques ou booléennes
        if any(keyword in line for keyword in ["true", "false", "null"]) or any(
            char.isdigit() for char in line
        ):
            return ORANGE

        # Par défaut
        return WHITE
