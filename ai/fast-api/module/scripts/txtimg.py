from IPython.display import display_png, Image
from torch import autocast
from diffusers import StableDiffusionPipeline
#from japanese_stable_diffusion import JapaneseStableDiffusionPipeline

#@title Settings
#access_token = "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"  #@param {type:"string"}

pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4").to("cuda")
#pipe = JapaneseStableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4").to("cuda")

#@title Parameters
prompt = "car,doll"

#parr = prompt.replace('、', ',').replace('。', ",") #.split(',')


# 画像を生成する。
with autocast("cuda"):
#  image = pipe(parr).images[0]
   image = pipe(prompt).images[0]
# 画像を保存する。
file_name = "exampl.png"
image.save(file_name)

# 画像を表示する。
#display_png(Image(file_name))
