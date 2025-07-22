from manim import BLUE, DOWN, SVGMobject, Text, VGroup

from cs_manim.style import FONT_NAME


class Cloud(VGroup):
    def __init__(
        self,
        text="Cloud",
        color=BLUE,
    ):
        """
        Create a cloud object for representing cloud computing using Manim shapes

        Args:
            text: Text to display in the center of the cloud (default "Cloud")
            color: Color of the cloud (default "#87CEEB")

        Returns:
            VGroup: The group of objects representing the cloud
        """
        cloud = SVGMobject(
            "cs_manim/svg/cloud.svg",
            fill_color=color,
            fill_opacity=0.3,
            stroke_color=color,
            stroke_width=4,
        )

        cloud_text = Text(text, color=color, font=FONT_NAME).next_to(cloud, DOWN)

        cloud_group = VGroup(cloud, cloud_text)

        super().__init__(cloud_group)
