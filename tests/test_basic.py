"""Tests for imports and basic configuration."""


def test_package_import():
    """Test that the package can be imported with its metadata."""
    import cs_manim

    assert cs_manim.__version__ == "0.1.0"
    assert cs_manim.__author__ == "Pierre-Olivier Brillant"


def test_objects_import():
    """Test that the main objects can be imported."""
    from cs_manim.objects import (
        AndroidLogo,
        AppleLogo,
        MobilePhone,
        PortableComputer,
        Server,
    )

    # Verify that the classes exist
    assert AndroidLogo is not None
    assert AppleLogo is not None
    assert PortableComputer is not None
    assert Server is not None
    assert MobilePhone is not None


def test_style_import():
    """Test that the style constants can be imported."""
    from cs_manim.style import (
        CLIENT_COLOR,
        FONT_NAME,
        REQUEST_COLOR,
        RESPONSE_COLOR,
        SERVER_COLOR,
    )

    # Verify that the constants exist
    assert CLIENT_COLOR is not None
    assert SERVER_COLOR is not None
    assert REQUEST_COLOR is not None
    assert RESPONSE_COLOR is not None
    assert FONT_NAME == "Inconsolata"


def test_public_api():
    """Test that the public API is accessible via the main package."""
    import cs_manim

    # Verify that the main objects are accessible
    assert hasattr(cs_manim, "AndroidLogo")
    assert hasattr(cs_manim, "AppleLogo")
    assert hasattr(cs_manim, "PortableComputer")
    assert hasattr(cs_manim, "Server")
    assert hasattr(cs_manim, "MobilePhone")

    # Verify that the styles are accessible
    assert hasattr(cs_manim, "CLIENT_COLOR")
    assert hasattr(cs_manim, "SERVER_COLOR")
    assert hasattr(cs_manim, "FONT_NAME")
