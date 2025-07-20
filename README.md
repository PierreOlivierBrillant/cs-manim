# CS-Manim

Video animations with Manim to explain technical concepts related to computer science.

## Description

CS-Manim is a Python library that provides reusable objects and styles to create educational animations with Manim, specially designed to explain computer science and programming concepts.

## Installation

```bash
pip install cs-manim
```

## Usage

```python
from manim import *
from cs_manim import Computer, Server, MobilePhone, HttpCall
from cs_manim import CLIENT_COLOR, SERVER_COLOR, FONT_NAME

class MyScene(Scene):
    def construct(self):
        # Create objects for your animations
        computer = Computer("PC Client")
        server = Server("API Server")
        mobile = MobilePhone("Smartphone")
        api_call = HttpCall("POST", "/api/users")

        # Position and animate
        computer.shift(LEFT * 3)
        server.shift(RIGHT * 3)

        self.play(Create(computer))
        self.play(Create(server))
        self.play(Create(api_call))
```

## Features

- **Reusable objects**: Computers, servers, mobile phones, HTTP calls
- **Consistent styles**: Predefined colors and fonts
- **Manim compatible**: Uses Manim 0.19.0+
- **Easy to use**: Simple import and intuitive API

## Available Objects

### PortableComputer

```python
computer = PortableComputer(name="My PC", color=CLIENT_COLOR)
```

### Server

```python
server = Server(name="My Server", color=SERVER_COLOR)
```

### MobilePhone

```python
mobile = MobilePhone(name="My Phone", color=PURPLE)
```

### HttpCall

```python
http_call = HttpCall(method="POST", url="/api/users", color=ORANGE)
```

### AndroidLogo

```python
android = AndroidLogo(color=GREEN)
```

### AppleLogo

```python
apple = AppleLogo(color=WHITE)
```

### Database

```python
database = Database(name="My Database", color=BLUE)
```

### Cloud

```python
cloud = Cloud(name="My Cloud", color=GRAY)
```

### Monitor

```python
monitor = Monitor(name="My Monitor", color=BLACK)
```

### TestTube

```python
test_tube = TestTube(color=RED)
```

## Development

### Environment Setup

```bash
# Clone the repository
git clone https://github.com/PierreOlivierBrillant/cs-manim.git
cd cs-manim

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# or .venv\Scripts\activate  # Windows

# Install in development mode
pip install -e .[dev]
```

### Tests

```bash
# Run tests
pytest

# With coverage
pytest --cov=cs_manim
```

### Formatting and linting

```bash
# Format the code
black cs_manim tests examples

# Check style
ruff cs_manim tests examples

# Check types
mypy cs_manim
```

### Package building

```bash
# Build the package
python -m build

# Check the package
twine check dist/*
```

## Publishing

### Prerequisites for publishing

1. PyPI account (https://pypi.org/)
2. PyPI API token configured
3. All checks passed

### Publishing steps

1. **Update version** in `pyproject.toml`
2. **Update CHANGELOG.md**
3. **Create git tag**: `git tag v0.1.0`
4. **Push the tag**: `git push origin v0.1.0`
5. **Create release on GitHub**

Publishing to PyPI happens automatically via GitHub Actions when creating a release.

### Manual publishing

```bash
# Build the package
python -m build

# Publish to PyPI
twine upload dist/*
```

## Examples

See the `examples/` folder for usage examples.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution instructions.

## Dependencies

- Python >= 3.10
- Manim >= 0.19.0
- Pillow >= 11.0.0
- NumPy >= 1.24.0
- SciPy >= 1.10.0

## License

MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Pierre-Olivier Brillant - pierreolivierbrillant@gmail.com

## Links

- [GitHub](https://github.com/PierreOlivierBrillant/cs-manim)
- [PyPI](https://pypi.org/project/cs-manim/)
- [Manim Documentation](https://docs.manim.community/)
