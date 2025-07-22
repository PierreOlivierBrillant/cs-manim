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
            color: Color of the server (default BLUE)

        Returns:
            VGroup: The group of objects representing the server
        """

        WIDTH = 1.6
        HEIGHT = 2
        LIGHT_RADIUS = 0.03 * WIDTH

        def create_light():
            return Circle(
                radius=LIGHT_RADIUS,
                color=color,
                fill_opacity=1,
            )

        def create_rack():
            return VGroup(
                Rectangle(
                    width=WIDTH * 0.9,
                    height=HEIGHT * 0.2,
                    color=color,
                    fill_opacity=0.1,
                ),
                create_light().shift(LEFT * (0.35 * WIDTH)),
                create_light().shift(LEFT * (0.25 * WIDTH)),
                create_light().shift(LEFT * (0.15 * WIDTH)),
                Rectangle(
                    width=(0.25 * WIDTH),
                    height=(0.05 * HEIGHT),
                    color=color,
                    fill_opacity=1,
                ).shift(RIGHT * (0.2 * WIDTH)),
            )

        main_case = Rectangle(
            width=WIDTH,
            height=HEIGHT,
            color=color,
            fill_opacity=0.3,
        )

        return super().__init__(
            main_case,
            # Top rack
            create_rack().shift(UP * (HEIGHT * 0.36)),
            # Middle rack
            create_rack().shift(UP * (HEIGHT * 0.12)),
            create_rack().shift(DOWN * (HEIGHT * 0.12)),
            # Bottom rack
            create_rack().shift(DOWN * (HEIGHT * 0.36)),
            # Server name
            Text(name, color=color, font=FONT_NAME).next_to(main_case, DOWN),
        )
