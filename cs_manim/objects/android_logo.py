from manim import SVGMobject, VGroup


class AndroidLogo(VGroup):
    def __init__(self):
        """
        Create an Android logo
        """
        super().__init__(SVGMobject("cs_manim/svg/android_logo.svg"))
