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
        monitor_frame = Rectangle(
            width=2.5, height=1.6, color=color, fill_opacity=0.3, stroke_width=3
        )

        monitor_screen = Rectangle(width=2.3, height=1.4, color=color, fill_opacity=0.1)

        stand_base = Rectangle(
            width=1.0, height=0.1, color=color, fill_opacity=0.5
        ).shift(DOWN * 1.05)

        stand_pole = Rectangle(
            width=0.1, height=0.2, color=color, fill_opacity=0.5
        ).shift(DOWN * 0.9)

        label = Text(name, font_size=16, color=color, font=FONT_NAME).shift(DOWN * 1.3)

        components = [monitor_frame, monitor_screen, stand_base, stand_pole, label]
        if content is not None:
            components.append(content)

        super().__init__(*components)
