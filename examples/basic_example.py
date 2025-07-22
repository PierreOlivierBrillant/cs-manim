"""
Example usage of the cs-manim library
"""

from manim import DOWN, LEFT, RIGHT, Arrow, Create, Scene

from cs_manim import PortableComputer, MobilePhone, Server


class BasicExample(Scene):
    def construct(self):
        # Create objects
        computer = PortableComputer("PC Client")
        server = Server("API Server")
        mobile = MobilePhone("Smartphone")

        # Position objects
        computer.shift(LEFT * 3)
        server.shift(RIGHT * 3)
        mobile.shift(DOWN * 2)

        # Add to scene
        self.play(Create(computer))
        self.play(Create(server))
        self.play(Create(mobile))

        # Communication animation
        arrow1 = Arrow(computer.get_right(), server.get_left())
        arrow2 = Arrow(server.get_left(), computer.get_right())

        self.play(Create(arrow1))
        self.wait(0.5)
        self.play(Create(arrow2))
        self.wait(2)


if __name__ == "__main__":
    # To run this scene, use:
    # manim examples/basic_example.py BasicExample
    pass
