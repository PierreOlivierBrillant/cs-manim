from manim import VGroup


class BaseObject(VGroup):
    """
    Base class for all objects in the scene.
    This class is used to define common methods and properties for all objects.
    """

    object: VGroup

    @property
    def object_right(self):
        return self.object.get_right()

    @property
    def object_left(self):
        return self.object.get_left()

    @property
    def object_top(self):
        return self.object.get_top()

    @property
    def object_bottom(self):
        return self.object.get_bottom()
