from PIL import Image

from src.add_creator.utils.round_rectange import round_rectangle

def create_rounded_image(image, radius) -> Image:

    mask = round_rectangle(
        image.size,
        radius=radius,
        fill="white",
    ).convert("L")

    image.putalpha(mask)

    return image