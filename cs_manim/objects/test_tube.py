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
        WIDTH = 3.0
        HEIGHT = 3.0

        def create_flask():
            return Polygon(
                [WIDTH * -0.5, HEIGHT * -0.5, 0],
                [WIDTH * -0.15, 0, 0],
                [WIDTH * -0.15, HEIGHT * 0.4, 0],
                [WIDTH * -0.2, HEIGHT * 0.5, 0],
                [WIDTH * 0.2, HEIGHT * 0.5, 0],
                [WIDTH * 0.15, HEIGHT * 0.4, 0],
                [WIDTH * 0.15, 0, 0],
                [WIDTH * 0.5, HEIGHT * -0.5, 0],
                fill_color=color,
                fill_opacity=0,
                stroke_color=color,
            ).round_corners(WIDTH * 0.05)

        mask = (
            Rectangle(width=WIDTH, height=HEIGHT, fill_color=color)
            .set_stroke(color, width=WIDTH)
            .shift(UP * (HEIGHT * 0.4))
        )

        flask_content = (
            Difference(create_flask(), mask)
            .set_color(color)
            .set_opacity(0.6)
            .set_stroke(color, width=0)
        )

        super().__init__(create_flask(), flask_content)
