from manim import RED, UP, Difference, Polygon, Rectangle, VGroup


class TestTube(VGroup):
    def __init__(self, name="Tests", color=RED):
        """
        Create a test tube to represent tests

        Args:
            name: Name of the test tube (default "Tests")
            color: Color of the test tube (default RED)

        Returns:
            VGroup: The group of objects representing test tube
        """

        def create_flask():
            return Polygon(
                [-0.5, 0, 0],
                [-0.15, 0.5, 0],
                [-0.15, 0.9, 0],
                [-0.2, 1, 0],
                [0.2, 1, 0],
                [0.15, 0.9, 0],
                [0.15, 0.5, 0],
                [0.5, 0, 0],
                fill_color=color,
                fill_opacity=0,
                stroke_width=8,
                stroke_color=color,
            ).round_corners(0.05)

        mask = (
            Rectangle(width=1.0, height=1.0, fill_color=color)
            .set_stroke(color, width=1)
            .shift(UP * 0.9)
        )

        flask_content = (
            Difference(create_flask(), mask)
            .set_color(color)
            .set_opacity(0.6)
            .set_stroke(color, width=0)
        )

        super().__init__(create_flask(), flask_content)
