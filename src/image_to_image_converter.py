
import base64
import requests
import base64
import config

def convert_img_to_base64_str(image_bytes: bytes) -> bytes:

    base64img = base64.b64encode(image_bytes)

    return base64img.decode("ascii")

def create_similar_image_from_image_bytes(
    image_bytes: bytes, 
    prompt: str, 
    color: str
):

    payload={
        "init_images": [convert_img_to_base64_str(image_bytes)],
        "steps": config.STABLE_DIFFUSION_STEPS,
        "resize_mode": config.STABLE_DIFFUSION_RESIZE_MODE,
        "prompt": f"(color:{color}) {prompt}",
        "negative_prompt": config.STABLE_DIFFUSION_DEFAULT_NEGATIVE_PROMPT,
    }

    response = requests.post(
        url=f"{config.STABLE_DIFFUSION_URL}/sdapi/v1/img2img",
        json=payload,
    )

    created_image_bytes = base64.b64decode(response.json()["images"][0])

    return created_image_bytes