from manim import DOWN, Mobject, Rectangle, Text, VGroup

from ..style import CLIENT_COLOR, FONT_NAME


class Monitor(VGroup):
    def __init__(
        self, name="Monitor", color=CLIENT_COLOR, content: Mobject | None = None
    ):
        """
        Create a monitor/screen

        Args:
            name: Name of the monitor (default "Monitor")
            color: Color of the monitor (default CLIENT_COLOR)
            content: Content to display on the monitor screen (default None)

        Returns:
            VGroup: The group of objects representing the monitor
        """

        WIDTH = 2
        HEIGHT = 1.28

        monitor_frame = Rectangle(
            width=WIDTH, height=HEIGHT, color=color, fill_opacity=0.3, stroke_width=3
        )

        monitor_screen = Rectangle(
            width=WIDTH * 0.92, height=HEIGHT * 0.875, color=color, fill_opacity=0.1
        )

        stand_pole = Rectangle(
            width=WIDTH * 0.04, height=HEIGHT * 0.125, color=color, fill_opacity=0.5
        ).next_to(monitor_frame, DOWN, buff=0.01)

        stand_base = Rectangle(
            width=0.4 * WIDTH, height=HEIGHT * 0.0625, color=color, fill_opacity=0.5
        ).next_to(stand_pole, DOWN, buff=0.01)

        label = Text(name, color=color, font=FONT_NAME).next_to(stand_base, DOWN)

        components = [monitor_frame, monitor_screen, stand_base, stand_pole, label]
        if content is not None:
            components.append(content)

        super().__init__(*components)
