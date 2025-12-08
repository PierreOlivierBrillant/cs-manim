from importlib import resources

from manim import SVGMobject

from cs_manim.objects.base_object import BaseObject


class AngularLogo(BaseObject):
    def __init__(self):
        """
        Create an Angular logo
        """
        with resources.path("cs_manim.svg", "angular_logo.svg") as svg_path:
            super().__init__(SVGMobject(svg_path))
