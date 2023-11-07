from PIL import Image, ImageDraw, ImageFont

def create_text(text, font: ImageFont, font_color=(255, 0, 0)) -> Image:

    (width, height), (offset_x, offset_y) = font.font.getsize(text)
    width, height = font.getmask(text).size

    image = Image.new(mode="RGBA", size=(width, height))

    draw = ImageDraw.Draw(image)

    coordinates = (- offset_x, - offset_y)

    draw.text(coordinates, text, fill=font_color, font=font)

    return image