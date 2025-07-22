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
        DISK_WIDTH = 3
        DISK_HEIGHT = 0.75

        def create_arc():
            return Arc(
                radius=DISK_WIDTH / 2, start_angle=PI, angle=PI, color=color
            ).stretch(DISK_HEIGHT / DISK_WIDTH, 1)
            # .shift(UP * 0.83 * (DISK_HEIGHT * 3) / 2)

        top_disk = Ellipse(
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
        half_ellipse.next_to(mask, DOWN, buff=-0.001)

        top_arc = create_arc().next_to(top_disk, DOWN, buff=DISK_HEIGHT / 2)
        middle_arc = create_arc().next_to(top_disk, DOWN, buff=DISK_HEIGHT * 1.5)
        bottom_arc = create_arc().next_to(mask, DOWN, buff=-0.01)

        label = Text(name, color=color, font=FONT_NAME).next_to(bottom_arc, DOWN)

        super().__init__(
            main_body,
            top_disk,
            main_body_left_edge,
            main_body_right_edge,
            top_arc,
            middle_arc,
            bottom_arc,
            half_ellipse,
            label,
        )
