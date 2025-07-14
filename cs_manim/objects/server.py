from manim import BLUE, DOWN, LEFT, RIGHT, UP, Circle, Rectangle, Text, VGroup

from ..style import FONT_NAME


class Server(VGroup):
    def __init__(
        self,
        name="Server",
        color=BLUE,
    ):
        """
        Create a server

        Args:
            name: Name of the server (default "Server")
            color: Color of the server (default GREEN)

        Returns:
            VGroup: The group of objects representing the server
        """
        LIGHT_RADIUS = 0.03

        def create_light():
            return Circle(radius=LIGHT_RADIUS, color=color, fill_opacity=1)

        def create_rack():
            return VGroup(
                Rectangle(width=0.9, height=0.25, color=color, fill_opacity=0.1),
                create_light().shift(LEFT * 0.35),
                create_light().shift(LEFT * 0.25),
                create_light().shift(LEFT * 0.15),
                Rectangle(width=0.3, height=0.05, color=color, fill_opacity=1).shift(
                    RIGHT * 0.2
                ),
            )

        return super().__init__(
            # Main case
            Rectangle(width=1.0, height=1.25, color=color, fill_opacity=0.3),
            # Top rack
            create_rack().shift(UP * 0.45),
            # Middle rack
            create_rack().shift(UP * 0.15),
            create_rack().shift(DOWN * 0.15),
            # Bottom rack
            create_rack().shift(DOWN * 0.45),
            # Server name
            Text(name, font_size=14, color=color, font=FONT_NAME).shift(DOWN * 0.8),
        )
