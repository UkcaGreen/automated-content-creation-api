from PIL import Image, ImageDraw, ImageFont

from src.add_creator.utils.round_rectange import round_rectangle

def create_button(text, font: ImageFont, font_color="white", button_color="red") -> Image:

    radius = font.size//2

    (width, height), (offset_x, offset_y) = font.font.getsize(text)

    rect = round_rectangle(
        size=(width + font.size, height + font.size),
        radius=radius,
        fill=button_color,
    )

    draw = ImageDraw.Draw(rect)

    coordinates = (
        rect.size[0]//2 - width//2 - offset_x, 
        rect.size[1]//2 - height//2 - offset_y, 
    )

    draw.text(coordinates, text, fill=font_color, font=font)

    mask = round_rectangle(
        rect.size,
        radius=radius,
        fill="white",
    ).convert("L")

    rect.putalpha(mask)

    return rect