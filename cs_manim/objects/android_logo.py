from manim import SVGMobject

from cs_manim.objects.base_object import BaseObject


class AndroidLogo(BaseObject):
    def __init__(self):
        """
        Create an Android logo
        """
        super().__init__(SVGMobject("cs_manim/svg/android_logo.svg"))
