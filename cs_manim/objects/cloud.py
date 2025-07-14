from manim import BLUE, DOWN, SVGMobject, Text, VGroup


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
        # Créer un fond blanc avec la même forme
        cloud = (
            SVGMobject("cs_manim/svg/cloud.svg")
            .set_fill(color, opacity=0.3)
            .set_stroke(color, width=7)
        )

        cloud_text = Text(text, font_size=24, color=color).shift(DOWN * 0.2)

        cloud_group = VGroup(cloud, cloud_text)

        super().__init__(cloud_group)
