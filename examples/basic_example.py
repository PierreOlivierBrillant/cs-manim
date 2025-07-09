"""
Exemple d'utilisation de la librairie cs-manim
"""

from manim import Scene, RIGHT, DOWN, LEFT, Create, Arrow
from cs_manim import Computer, Server, MobilePhone
from cs_manim import CLIENT_COLOR, SERVER_COLOR


class BasicExample(Scene):
    def construct(self):
        # Créer les objets
        computer = Computer("PC Client")
        server = Server("API Server")
        mobile = MobilePhone("Smartphone")

        # Positionner les objets
        computer.shift(LEFT * 3)
        server.shift(RIGHT * 3)
        mobile.shift(DOWN * 2)

        # Ajouter à la scène
        self.play(Create(computer))
        self.play(Create(server))
        self.play(Create(mobile))

        # Animation de communication
        arrow1 = Arrow(computer.get_right(), server.get_left(), color=CLIENT_COLOR)
        arrow2 = Arrow(server.get_left(), computer.get_right(), color=SERVER_COLOR)

        self.play(Create(arrow1))
        self.wait(0.5)
        self.play(Create(arrow2))
        self.wait(2)


if __name__ == "__main__":
    # Pour exécuter cette scène, utilisez :
    # manim examples/basic_example.py BasicExample
    pass
