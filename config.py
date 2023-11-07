from pathlib import Path
from PIL import ImageFont
import os

UPLOADS_DIR = Path() / "static" / "uploads"
CREATED_IMAGES_DIR = Path() / "static" /  "created_images"
CREATED_ADS_DIR = Path() / "static" /  "created_ads"

STABLE_DIFFUSION_URL = "http://127.0.0.1:7860"
STABLE_DIFFUSION_STEPS = 32
STABLE_DIFFUSION_RESIZE_MODE = 1
STABLE_DIFFUSION_DEFAULT_NEGATIVE_PROMPT = "distorted image, distortion, dismorph, ugly, broken, incomplete, missing, blurry, faded, foggy, ambigious, unrealistic, fantasy, amateur"

AD_CREATION_DEFAULT_FONT = ImageFont.truetype("src/add_creator/assets/fonts/OpenSans-Bold.ttf", 28)

os.makedirs(UPLOADS_DIR, exist_ok=True)
os.makedirs(CREATED_IMAGES_DIR, exist_ok=True)
os.makedirs(CREATED_ADS_DIR, exist_ok=True)