from manim import DOWN, PURPLE, Rectangle, RoundedRectangle, Text, VGroup

from ..style import FONT_NAME


class MobilePhone(VGroup):
    def __init__(self, name="Mobile", color=PURPLE):
        """
        Create a mobile phone

        Args:
            name: Name of the phone (default "Mobile")
            color: Color of the phone (default PURPLE)

        Returns:
            VGroup: The group of objects representing the mobile phone
        """
        return super().__init__(
            RoundedRectangle(
                width=0.8,
                height=1.4,
                color=color,
                fill_opacity=0.3,
                corner_radius=0.1,
            ),
            Rectangle(width=0.6, height=1.2, color=color, fill_opacity=0.1),
            Text(name, font_size=16, color=color, font=FONT_NAME).shift(DOWN * 0.9),
        )
