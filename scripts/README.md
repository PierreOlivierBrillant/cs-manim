# Scripts

This folder contains utility scripts for the CS-Manim project.

## export_objects.py

Export all CS-Manim objects as images.

### Usage

```bash
# Basic export (PNG, high quality, output folder)
python scripts/export_objects.py

# Specify output folder
python scripts/export_objects.py --output-dir my_folder

# Change format and quality
python scripts/export_objects.py --format svg --quality production

# Help
python scripts/export_objects.py --help
```

### Options

- `--output-dir` : Output folder (default: `output`)
- `--format` : Image format (`png` or `svg`, default: `png`)
- `--quality` : Render quality (`low`, `medium`, `high`, `production`, default: `high`)

### Exported objects

The script automatically generates an image for each object:

#### Devices

- Monitor/Screen
- Portable computer
- Mobile phone

#### Infrastructure

- Servers
- Database
- Cloud

#### Network

- HTTP Call

#### Testing

- Test Tube

#### Logos

- Android Logo
- Apple Logo
