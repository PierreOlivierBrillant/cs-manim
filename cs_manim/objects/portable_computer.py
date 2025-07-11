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
        laptop_keyboard = Rectangle(width=2, height=1.2, color=color, fill_opacity=0.3)

        laptop_screen = Rectangle(
            width=2.2, height=0.2, color=color, fill_opacity=0.8
        ).shift(DOWN * 0.7)

        label = Text(name, font_size=16, color=color, font=FONT_NAME).shift(DOWN * 1.0)

        components = [laptop_keyboard, laptop_screen, label]
        if content is not None:
            components.append(content)

        super().__init__(components)
