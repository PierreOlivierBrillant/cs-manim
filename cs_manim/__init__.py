"""
CS-Manim: Video animations with Manim to explain technical concepts
related to computer science.

This library provides reusable objects and styles to create
educational animations with Manim, specially designed to explain
computer science concepts.
"""

from .objects import (
    AndroidLogo,
    AppleLogo,
    Cloud,
    Database,
    MobilePhone,
    Monitor,
    PortableComputer,
    Server,
    TestTube,
)
from .style import CLIENT_COLOR, FONT_NAME, REQUEST_COLOR, RESPONSE_COLOR, SERVER_COLOR

__version__ = "0.1.0"
__author__ = "Pierre-Olivier Brillant"
__email__ = "pierreolivierbrillant@gmail.com"

__all__ = [
    "AndroidLogo",
    "AppleLogo",
    "Cloud",
    "Database",
    "Monitor",
    "PortableComputer",
    "Server",
    "MobilePhone",
    "TestTube",
    "CLIENT_COLOR",
    "SERVER_COLOR",
    "REQUEST_COLOR",
    "RESPONSE_COLOR",
    "FONT_NAME",
]
