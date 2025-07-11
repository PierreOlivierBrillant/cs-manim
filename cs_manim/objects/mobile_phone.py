from manim import DOWN, PURPLE, Mobject, Rectangle, RoundedRectangle, Text, VGroup

from ..style import FONT_NAME


class MobilePhone(VGroup):
    def __init__(self, name="Mobile", color=PURPLE, content: Mobject | None = None):
        """
        Create a mobile phone

        Args:
            name: Name of the phone (default "Mobile")
            color: Color of the phone (default PURPLE)
            content: Content to display on the phone (default None)

        Returns:
            VGroup: The group of objects representing the mobile phone
        """
        phone_body = RoundedRectangle(
            width=0.8,
            height=1.4,
            color=color,
            fill_opacity=0.3,
            corner_radius=0.1,
        )
        phone_screen = Rectangle(width=0.6, height=1.2, color=color, fill_opacity=0.1)
        label = Text(name, font_size=16, color=color, font=FONT_NAME).shift(DOWN * 0.9)

        components = [phone_body, phone_screen, label]
        if content is not None:
            components.append(content)

        super().__init__(*components)
