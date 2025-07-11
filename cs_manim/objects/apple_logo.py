from manim import SVGMobject, VGroup


class AppleLogo(VGroup):
    def __init__(self):
        """
        Create an Apple logo
        """
        super().__init__(SVGMobject("cs_manim/svg/apple_logo.svg"))
