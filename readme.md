### Description

This endpoint is created as a prototype for automated content creation application. It takes an example image and creates a similar image by using Stable Diffusion. After that it combines some logos and text to form a programmatically generated content.

### How to run?

> Note: this application requires Stable Diffusion ([you can get it here](https://github.com/AUTOMATIC1111/stable-diffusion-webui)) running with `--api` flag. If stable diffusion is running at an address other than `http://127.0.0.1:7860`, please update `STABLE_DIFFUSION_URL` variable in `config.py`.

1. install requirements

`pip install -r requirements.txt`

2. start the application

`uvicorn main:app --reload`

3. navigate to application in your browser

Open `http://127.0.0.1:8000` at your browser, if you see `{"status": "ok"}``, installation is successful.

4. navigate to url endpoints

Navigate to `http://127.0.0.1:8000/docs` at your browser, you will see awailable endpoints there. You can use these endpoints by clicking `Try it out` buttons.

### Dev Logs

#### Handling Hex Codes

System also supports passing colors to use during both image and content creation. However Stable Diffusion was not that familiar with hex codes, rather it recognizes human readable color names. So hex codes are converted into human readable names by using `webcolors` library.

#### Constructing content

Content consists logo, image, text, and a button. In order to contruct the image, first each of the elements are generated separately and they gets poisitioned on a white canvas. All of these image manipulations are made by `pillow` library (a.k.a. `PIL`).

#### Installing Stable Diffusion

In this project web api of Stable stable-diffusion-webui by AUTOMATIC1111 is used. [You can get it here](https://github.com/AUTOMATIC1111/stable-diffusion-webui).

#### Used checkpoints

These checkpoints are used in development and testing of this project: https://huggingface.co/stabilityai/stable-diffusion-2-1