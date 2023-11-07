from PIL import Image, ImageFont

from src.add_creator.components.button import create_button
from src.add_creator.components.text import create_text
from src.add_creator.components.rounded_image import create_rounded_image

def create_ad(
    logo: Image,
    image: Image,
    punchline: str,
    punchline_font_color: str, #hexcode
    font: ImageFont,
    button_text: str,
    button_color: str, #hexcode
    button_font_color: str = "white",
) -> Image:
    
    bg = Image.new(mode="RGBA", size=(1024,1024), color="white")
    
    logo.thumbnail((200,200), Image.LANCZOS)

    image.thumbnail((512,512), Image.LANCZOS)
    image = create_rounded_image(image=image, radius=32)

    punchline = create_text(
        text=punchline,
        font=font,
        font_color=punchline_font_color,
    )

    button = create_button(
        text=button_text,
        font=font,
        font_color=button_font_color,
        button_color=button_color,
    )

    bg.paste(
        logo,
        (  
            bg.size[0]//2 - logo.size[0]//2,
            bg.size[1]//16 * 2 - logo.size[1]//2,
        ),
        logo,
    )

    bg.paste(
        image,
        (  
            bg.size[0]//2 - image.size[0]//2,
            bg.size[1]//16 * 8 - image.size[1]//2,
        ),
        image,
    )

    bg.paste(
        punchline,
        (  
            bg.size[0]//2 - punchline.size[0]//2,
            bg.size[1]//32 * 27 - punchline.size[1]//2,
        ),
        punchline,
    )

    bg.paste(
        button,
        (  
            bg.size[0]//2 - button.size[0]//2,
            bg.size[1]//16 * 15 - button.size[1]//2,
        ),
        button,
    )

    return bg