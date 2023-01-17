import os
import deepl 
from IPython.display import display_png, Image
from torch import autocast
from diffusers import StableDiffusionPipeline
import paramiko
from dotenv import load_dotenv

load_dotenv()

#KEY
DEEPL_KEY=os.getenv("DEEPL_KEY")
#SCP
HOST=os.getenv("HOST")
PORT=os.getenv("PORT")
USER=os.getenv("USER")
KEY_FILE=os.getenv("KEY_FILE")

#main
def generate(keyword:str, file_name: str):
    try:
        #split
        s_text=keyword.split(",")

        #translate to English
        translator = deepl.Translator(DEEPL_KEY) 
        translated_text = []

        for text in s_text:
            result = translator.translate_text(text, target_lang='EN-GB') 
            translated_text.append(result.text)

        #join
        j_text=','.join(translated_text)

        #generate img
        result=generate_img(j_text, file_name)
        if result == "error": 
            return "error"

        #send in scp
        scp_flag = scp_img(file_name)
        if scp_flag == "error":
            return "error"

        return 
    except:
        return "error"

#stablediffusion
def generate_img(text: str,file_name: str):
    try:
        pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4").to("cuda")

        #@title Parameters
        prompt = "Realistic,unreal engine," + text+",4K/8K"
        print(prompt)
        # prompt = text

        # 画像を生成する。
        with autocast("cuda"):
            image = pipe(
                prompt,
                num_inference_steps=75
            ).images[0]
        # 画像を保存する。
        image.save("images/"+ file_name)
        # 画像を表示する。 
        return 
    except:
        print("stablediffusion error")
        return "error"

#transfer img file to VM-web01
def scp_img(file_name: str):
    import scp
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(HOST, PORT, USER, key_filename=KEY_FILE,timeout=5.0)

        with scp.SCPClient(ssh.get_transport()) as scp:
            scp.put("images/"+file_name, '/usr/share/nginx/html/images/')
        ssh.close()
        del ssh
        return "success"
    except:
        return "error"
