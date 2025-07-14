from manim import (
    BLUE,
    DOWN,
    PI,
    UP,
    Arc,
    Difference,
    Ellipse,
    Line,
    Rectangle,
    Text,
    VGroup,
)

from ..style import FONT_NAME


class Database(VGroup):
    def __init__(self, name="Database", color=BLUE):
        """
        Create a database with 3 stacked disks

        Args:
            name: Name of the database (default "Database")
            color: Color of the database (default SERVER_COLOR)

        Returns:
            VGroup: The group of objects representing the database
        """
        DISK_WIDTH = 0.8
        DISK_HEIGHT = 0.2

        def create_arc():
            return (
                Arc(radius=DISK_WIDTH / 2, start_angle=PI, angle=PI, color=color)
                .stretch(DISK_HEIGHT / DISK_WIDTH, 1)
                .shift(UP * 0.83 * (DISK_HEIGHT * 3) / 2)
            )

        top_disk_top = Ellipse(
            width=DISK_WIDTH,
            height=DISK_HEIGHT,
            color=color,
            fill_opacity=1.0,
            stroke_color=color,
        ).shift(UP * (DISK_HEIGHT + DISK_HEIGHT / 2))

        main_body = Rectangle(
            width=DISK_WIDTH,
            height=DISK_HEIGHT * 3,
            color=color,
            fill_opacity=0.6,
            stroke_width=0,
        )

        main_body_left_edge = Line(
            start=main_body.get_left() + UP * (DISK_HEIGHT * 3) / 2,
            end=main_body.get_left() + DOWN * (DISK_HEIGHT * 3) / 2,
            color=color,
        )

        main_body_right_edge = Line(
            start=main_body.get_right() + UP * (DISK_HEIGHT * 3) / 2,
            end=main_body.get_right() + DOWN * (DISK_HEIGHT * 3) / 2,
            color=color,
        )

        ellipse = Ellipse(
            width=DISK_WIDTH,
            height=DISK_HEIGHT,
        ).shift(DOWN * (DISK_HEIGHT * 3) / 2)

        mask = Rectangle(
            width=DISK_WIDTH,
            height=DISK_HEIGHT,
            stroke_width=0,
            fill_color=color,
            fill_opacity=1.0,
        ).shift(DOWN * (DISK_HEIGHT * 3) / 2 + UP * (DISK_HEIGHT / 2))

        half_ellipse = Difference(ellipse, mask)
        half_ellipse.set_fill(color, opacity=0.6)
        half_ellipse.set_stroke(color, width=0)
        half_ellipse.shift(UP * 0.0002)

        top_arc = create_arc()
        middle_arc = create_arc().shift(
            DOWN * (DISK_HEIGHT * 3) / 2 - DOWN * (DISK_HEIGHT / 2)
        )
        bottom_arc = create_arc().shift(
            DOWN * (DISK_HEIGHT * 3) / 2 + DOWN * (DISK_HEIGHT / 2) - DOWN * 0.001
        )

        label = Text(name, font_size=16, color=color, font=FONT_NAME).shift(DOWN * 0.55)

        super().__init__(
            main_body,
            top_disk_top,
            main_body_left_edge,
            main_body_right_edge,
            top_arc,
            middle_arc,
            bottom_arc,
            half_ellipse,
            label,
        )
