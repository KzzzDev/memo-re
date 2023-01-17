from IPython.display import display_png, Image
from torch import autocast
from diffusers import StableDiffusionPipeline

def generate_img(text):
    try:
        pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4").to("cuda")

        #@title Parameters
        prompt = text

        # 画像を生成する。
        with autocast("cuda"):
            image = pipe(prompt).images[0]
        
        # 画像を保存する。
        file_name = "exampl.png"
        image.save(file_name)

        # 画像を表示する。
        return "success"
    except:
        return "error"