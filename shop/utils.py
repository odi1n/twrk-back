from pathlib import Path

from PIL import Image


def convert_image_to_webp(image_path) -> str:
    """
    Convert image to webp format
    """
    image_path = Path(image_path)
    image_name = image_path.stem
    image_format = image_path.suffix[1:]

    if image_format in ['png', 'jpg', 'jpeg']:
        image = Image.open(image_path)
        image.save(image_path.parent / (image_name + '.webp'), 'webp')
        return image_name + '.webp'
