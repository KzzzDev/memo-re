import os
import deepl 
from IPython.display import display_png, Image
from torch import autocast
from diffusers import StableDiffusionPipeline
import paramiko
import datetime
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
def generate(keyword:str, user_id: str):
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
        file_name=generate_img(j_text, user_id)
        if file_name == "error": 
            return "error"

        #send in scp
        scp_flag = scp_img(file_name)
        if scp_flag == "error":
            return "error"


        response = file_name
        return response
    except:
        return "error"

#stablediffusion
def generate_img(text: str,user_id: str):
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
        #generate name
        time = datetime.datetime.now()
        format_time = time.strftime("%Y-%m-%d_%H-%M-%S")
        # 画像を保存する。
        file_name = user_id + "_" + format_time + ".png"
        image.save("images/"+file_name)
        # 画像を表示する。 
        return file_name
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
            scp.put("images/"+file_name, '/usr/share/nginx/html/media/brain')
            #scp.put("images/"+file_name, '/home/th458-user/images')
        ssh.close()
        del ssh
        return "success"
    except:
        return "error"
