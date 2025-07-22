from manim import DOWN, Mobject, Rectangle, Text, VGroup

from ..style import CLIENT_COLOR, FONT_NAME


class PortableComputer(VGroup):
    def __init__(
        self, name="Computer", color=CLIENT_COLOR, content: Mobject | None = None
    ):
        """
        Create a Computer

        Args:
            name: Name of the computer
            color: Color of the client (default BLUE)
        """
        WIDTH = 2
        HEIGHT = 1.2

        laptop_screen = Rectangle(
            width=WIDTH, height=HEIGHT, color=color, fill_opacity=0.3
        )

        laptop_keyboard = Rectangle(
            width=WIDTH * 1.1, height=HEIGHT * 0.17, color=color, fill_opacity=0.8
        ).next_to(laptop_screen, DOWN, buff=0.01)

        label = Text(name, color=color, font=FONT_NAME).next_to(laptop_keyboard, DOWN)

        components = [laptop_keyboard, laptop_screen, label]
        if content is not None:
            components.append(content)

        super().__init__(components)
