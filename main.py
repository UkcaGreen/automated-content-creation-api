from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse
from src.add_creator import ad_creation
import requests
import config
from datetime import datetime
from uuid import uuid4
import base64
from io import BytesIO
from PIL import Image
from src.color_converter import get_closest_color
from src.image_to_image_converter import create_similar_image_from_image_bytes

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok"}

@app.post("/create_similar_image")
async def create_similar_image(
    uploaded_image: UploadFile, 
    prompt: str, 
    color: str
) -> FileResponse:

    data = await uploaded_image.read()

    file_name = f"{datetime.now().date().isoformat()}.{uuid4()}.{uploaded_image.filename.split('.')[-1]}"    

    with open(config.UPLOADS_DIR / file_name, "wb+") as f:
        f.write(data)

    created_image_bytes = create_similar_image_from_image_bytes(
        image_bytes=data,
        prompt=prompt,
        color=color,
    )

    with open(config.CREATED_IMAGES_DIR / file_name, "wb+") as f:
        f.write(created_image_bytes)

    return FileResponse(config.CREATED_IMAGES_DIR / file_name)


@app.post("/create_ad")
async def create_ad(
    uploaded_image: UploadFile,
    prompt: str,
    logo: UploadFile, 
    punchline: str,
    button: str,
    color: str, 
) -> FileResponse:

    file_name = f"{datetime.now().date().isoformat()}.{uuid4()}.{uploaded_image.filename.split('.')[-1]}" 

    uploaded_image_bytes =  await uploaded_image.read()

    with open(config.UPLOADS_DIR / file_name, "wb+") as f:
        f.write(uploaded_image_bytes)

    logo = Image.open(BytesIO(await logo.read()))

    created_image_bytes = create_similar_image_from_image_bytes(
        image_bytes=uploaded_image_bytes,
        prompt=prompt,
        color=color,
    )

    color = get_closest_color(color)

    created_image = Image.open(BytesIO(created_image_bytes))

    with open(config.CREATED_IMAGES_DIR / file_name, "wb+") as f:
        f.write(created_image_bytes)

    ad = ad_creation.create_ad(
        logo=logo,
        image=created_image,
        punchline=punchline,
        punchline_font_color=color,
        font=config.AD_CREATION_DEFAULT_FONT,
        button_text=button,
        button_color=color,
        button_font_color="white",
    )

    file_name_png = ".".join(file_name.split(".")[:-1] + ["png"])

    ad.save(config.CREATED_ADS_DIR / file_name_png)

    return FileResponse(config.CREATED_ADS_DIR / file_name_png)
    
