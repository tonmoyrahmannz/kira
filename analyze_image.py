#!/usr/bin/env python3
"""Analyze the screenshot image and describe what's visible."""
import subprocess
import sys
import json

image_path = "/Users/tonmoyrahman/.hermes/image_cache/img_0522ad00dfc4.jpg"

# Try to get image info with macOS built-in tools
try:
    result = subprocess.run(
        ["sips", "--getProperty", "all", image_path],
        capture_output=True, text=True, timeout=10
    )
    print("=== sips image info ===")
    print(result.stdout)
    if result.stderr:
        print("sips stderr:", result.stderr)
except Exception as e:
    print(f"sips error: {e}")

# Check if imagemagick is available
try:
    result = subprocess.run(
        ["identify", "-verbose", image_path],
        capture_output=True, text=True, timeout=10
    )
    print("\n=== ImageMagick identify ===")
    print(result.stdout[:2000])
except FileNotFoundError:
    print("\nImageMagick not available")
except Exception as e:
    print(f"identify error: {e}")

# Try python PIL
try:
    from PIL import Image
    img = Image.open(image_path)
    print(f"\n=== PIL Image info ===")
    print(f"Format: {img.format}")
    print(f"Size: {img.size[0]}x{img.size[1]}")
    print(f"Mode: {img.mode}")
except ImportError:
    print("\nPIL not available")
except Exception as e:
    print(f"PIL error: {e}")

# Try tesseract OCR if available
try:
    result = subprocess.run(
        ["tesseract", image_path, "stdout"],
        capture_output=True, text=True, timeout=30
    )
    print("\n=== Tesseract OCR output ===")
    print(result.stdout[:3000])
except FileNotFoundError:
    print("\nTesseract not available")
except Exception as e:
    print(f"Tesseract error: {e}")

# File command
try:
    result = subprocess.run(
        ["file", image_path],
        capture_output=True, text=True, timeout=5
    )
    print(f"\n=== file command ===")
    print(result.stdout)
except Exception as e:
    print(f"file error: {e}")
