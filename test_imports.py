# Test file pour vérifier l'organisation des imports
import os
import sys

from manim import Scene

from cs_manim import Computer, Server
from cs_manim.style import CLIENT_COLOR


def test_function():
    # Utilisons tous les imports pour qu'ils ne soient pas supprimés
    computer = Computer()
    server = Server()
    scene = Scene()
    color = CLIENT_COLOR
    path = os.path.join("test", "path")
    version = sys.version
    return computer, server, scene, color, path, version
