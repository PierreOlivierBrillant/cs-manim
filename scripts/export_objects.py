#!/usr/bin/env python3
"""
Script to export all cs_manim objects as images.

Usage:
    python scripts/export_objects.py [--output-dir OUTPUT_DIR] [--format FORMAT] [--quality QUALITY]

Examples:
    python scripts/export_objects.py
    python scripts/export_objects.py --output-dir output --format png --quality high
    python scripts/export_objects.py --format svg
"""

import argparse
from pathlib import Path

from manim import Scene, config

from cs_manim import (
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


class ObjectExportScene(Scene):
    """Scene to render individual objects for export."""

    def __init__(self, obj, name, **kwargs):
        self.obj = obj
        self.obj_name = name
        super().__init__(**kwargs)

    def construct(self):
        """Add the object to the scene."""
        self.add(self.obj)


def export_object_image(obj, name, output_dir, file_format="png", quality="medium"):
    """
    Export a single object as an image.

    Args:
        obj: The Manim object to export
        name: Name for the output file
        output_dir: Directory to save the image
        file_format: Image format (png, svg, etc.)
        quality: Render quality (low, medium, high, production)
    """
    # Configure Manim for image export
    original_format = config.format
    original_quality = config.quality
    original_output_file = config.output_file
    original_media_dir = config.media_dir

    try:
        # Set quality level
        quality_settings = {
            "low": "low_quality",
            "medium": "medium_quality",
            "high": "high_quality",
            "production": "production_quality",
        }
        config.quality = quality_settings.get(quality, "medium_quality")

        # Set format
        if file_format.lower() == "svg":
            config.format = "svg"
        else:
            config.format = "png"

        # Set output directory
        config.media_dir = str(output_dir)
        config.output_file = f"{name}"

        # Create and render scene
        scene = ObjectExportScene(obj, name)
        scene.render()

        print(f"✅ Exported {name}.{file_format}")

    except Exception as e:
        print(f"❌ Error exporting {name}: {e}")

    finally:
        # Restore original config
        config.format = original_format
        config.quality = original_quality
        config.output_file = original_output_file
        config.media_dir = original_media_dir


def create_objects():
    """Create all available objects with different configurations."""
    objects = [
        (AndroidLogo(), "android_logo"),
        (AppleLogo(), "apple_logo"),
        (Cloud(), "cloud"),
        (Database(), "database"),
        (Monitor(), "monitor"),
        (PortableComputer(), "portable_computer"),
        (Server(), "server"),
        (MobilePhone(), "mobile_phone"),
        (TestTube(), "test_tube"),
    ]

    return objects


def main():
    """Main function to export all objects."""
    parser = argparse.ArgumentParser(description="Export cs_manim objects as images")
    parser.add_argument(
        "--output-dir",
        default="output",
        help="Output directory for images (default: output)",
    )
    parser.add_argument(
        "--format",
        choices=["png", "svg"],
        default="png",
        help="Image format (default: png)",
    )
    parser.add_argument(
        "--quality",
        choices=["low", "medium", "high", "production"],
        default="high",
        help="Render quality (default: high)",
    )

    args = parser.parse_args()

    # Create output directory
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"🎯 Exporting objects to: {output_dir}")
    print(f"📐 Format: {args.format}")
    print(f"⚡ Quality: {args.quality}")
    print()

    # Create and export all objects
    objects = create_objects()

    for obj, name in objects:
        export_object_image(obj, name, output_dir, args.format, args.quality)

    print()
    print(f"✨ Export complete! {len(objects)} objects exported.")
    print(f"📁 Images saved in: {output_dir}")


if __name__ == "__main__":
    main()
