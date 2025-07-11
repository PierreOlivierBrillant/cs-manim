from manim import DOWN, GREEN, LEFT, RED, UP, YELLOW, Circle, Rectangle, Text, VGroup

from ..style import FONT_NAME, SERVER_COLOR


class Server(VGroup):
    def __init__(
        self,
        name="Server",
        color=SERVER_COLOR,
    ):
        """
        Create a server

        Args:
            name: Name of the server (default "Server")
            color: Color of the server (default GREEN)

        Returns:
            VGroup: The group of objects representing the server
        """
        return super().__init__(
            # Main case
            Rectangle(width=1.0, height=1.4, color=color, fill_opacity=0.3),
            # Top rack
            Rectangle(width=0.8, height=0.3, color=color, fill_opacity=0.1).shift(
                UP * 0.4
            ),
            Circle(radius=0.02, color=RED, fill_opacity=1).shift(UP * 0.4 + LEFT * 0.3),
            Circle(radius=0.02, color=GREEN, fill_opacity=1).shift(
                UP * 0.4 + LEFT * 0.2
            ),
            # Middle rack
            Rectangle(width=0.8, height=0.3, color=color, fill_opacity=0.1),
            Circle(radius=0.02, color=GREEN, fill_opacity=1).shift(LEFT * 0.3),
            Circle(radius=0.02, color=GREEN, fill_opacity=1).shift(LEFT * 0.2),
            # Bottom rack
            Rectangle(width=0.8, height=0.3, color=color, fill_opacity=0.1).shift(
                DOWN * 0.4
            ),
            Circle(radius=0.02, color=YELLOW, fill_opacity=1).shift(
                DOWN * 0.4 + LEFT * 0.3
            ),
            Circle(radius=0.02, color=GREEN, fill_opacity=1).shift(
                DOWN * 0.4 + LEFT * 0.2
            ),
            # Server name
            Text(name, font_size=14, color=color, font=FONT_NAME).shift(DOWN * 0.9),
        )
