from manim import SVGMobject

from cs_manim.objects.base_object import BaseObject


class AppleLogo(BaseObject):
    def __init__(self):
        """
        Create an Apple logo
        """
        super().__init__(SVGMobject("cs_manim/svg/apple_logo.svg"))
