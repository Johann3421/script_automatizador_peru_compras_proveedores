# -*- coding: utf-8 -*-
"""Genera un icono placeholder 16x16 y 32x32 en resources/icon.ico."""
import os
import sys
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESOURCES_DIR = os.path.join(ROOT, "resources")
ICON_PATH = os.path.join(RESOURCES_DIR, "icon.ico")


def _draw_icon(size: int) -> Image.Image:
    img = Image.new("RGBA", (size, size), (30, 136, 229, 255))
    draw = ImageDraw.Draw(img)
    margin = size // 8
    draw.rounded_rectangle(
        [margin, margin, size - margin, size - margin],
        radius=size // 8,
        outline=(255, 255, 255, 230),
        width=max(1, size // 16),
    )
    # Intentar escribir una "P" si hay una fuente disponible
    text = "P"
    for font_name in ("arial.ttf", "segoeui.ttf", "DejaVuSans-Bold.ttf"):
        try:
            font = ImageFont.truetype(font_name, size // 2)
            break
        except Exception:
            font = None
    else:
        font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = (size - tw) / 2 - bbox[0]
    y = (size - th) / 2 - bbox[1]
    draw.text((x, y), text, font=font, fill=(255, 255, 255, 255))
    return img


def main() -> int:
    os.makedirs(RESOURCES_DIR, exist_ok=True)
    if os.path.isfile(ICON_PATH):
        print(f"El icono ya existe: {ICON_PATH}")
        return 0
    sizes = [16, 32]
    imgs = [_draw_icon(s) for s in sizes]
    imgs[0].save(ICON_PATH, format="ICO", sizes=[(s, s) for s in sizes])
    print(f"Icono creado: {ICON_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
