from manim import DOWN, PURPLE, Mobject, RoundedRectangle, Text, VGroup

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

        WIDTH = 1.7
        HEIGHT = 3

        phone_body = RoundedRectangle(
            width=WIDTH,
            height=HEIGHT,
            color=color,
            fill_opacity=0.3,
            corner_radius=0.1,
        )
        phone_screen = RoundedRectangle(
            width=WIDTH * 0.75,
            height=HEIGHT * 0.857,
            color=color,
            fill_opacity=0.1,
            corner_radius=0.01,
        )
        label = Text(name, color=color, font=FONT_NAME).next_to(phone_body, DOWN)

        components = [phone_body, phone_screen, label]
        if content is not None:
            components.append(content)

        super().__init__(*components)
