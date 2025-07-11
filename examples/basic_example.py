"""
Example usage of the cs-manim library
"""

from manim import DOWN, LEFT, RIGHT, Arrow, Create, Scene

from cs_manim import CLIENT_COLOR, SERVER_COLOR, Computer, MobilePhone, Server


class BasicExample(Scene):
    def construct(self):
        # Create objects
        computer = Computer("PC Client")
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
        arrow1 = Arrow(computer.get_right(), server.get_left(), color=CLIENT_COLOR)
        arrow2 = Arrow(server.get_left(), computer.get_right(), color=SERVER_COLOR)

        self.play(Create(arrow1))
        self.wait(0.5)
        self.play(Create(arrow2))
        self.wait(2)


if __name__ == "__main__":
    # To run this scene, use:
    # manim examples/basic_example.py BasicExample
    pass
