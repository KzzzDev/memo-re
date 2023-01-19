# AI画像用VMの構築とAPI仕様について

## AzureでVMを作成

### OS
Linux
### イメージ
Data Science Virtual Machine - Ubuntu 20.04 - Gen2
### サイズ
Standard NC6s v3 (6 vcpu 数、112 GiB メモリ)
### ディスク
Premium SSD(ローカル冗長ストレージ)
### 管理
自動シャットダウン
Not enabled

## VM内にAI画像生成実行環境を作成

### ホームディレクトリ直下で作業ディレクトリを作成
```
mkdir diffusion-ai
cd diffusion-ai
```

### Stable Diffusionのgithubから最新のdiffusers.gitをクローン
```
git clone https://github.com/huggingface/diffusers.git
```
### condaの仮想実行環境の構築とテスト
```
cd /diffusion-ai/stable-diffusion
```
### condaの初期化(bashで環境変数パスに読み込まれるモジュールを更新)
```
conda init bash
```
### yaml設定ファイルを編集する。

基本デフォルトのまま

### yaml記載内容

依存関係
- python=3.8.5
- pip=20.3
- cudatoolkit=11.3
- pytorch=1.11.0
- torchvision=0.12.0
- numpy=1.19.2

pipでインポートするライブラリ
- albumentations==0.4.3
- albumentations==0.4.3
- diffusers
- opencv-python==4.1.2.30
- pudb==2019.2
- invisible-watermark
- imageio==2.9.0
- imageio-ffmpeg==0.4.2
- pytorch-lightning==1.4.2
- omegaconf==2.1.1
- test-tube>=0.7.5
- streamlit>=0.73.1
- einops==0.3.0
- torch-fidelity==0.3.0
- transformers==4.19.2
- torchmetrics==0.6.0
- kornia==0.6
- git+https://github.com/rinnakk/japanese-stable-diffusion.git
- -e git+https://github.com/CompVis/taming-transformers.git@master#egg=taming-transformers
- -e git+https://github.com/openai/CLIP.git@main#egg=clip
- -e .

※新規にライブラリモジュールを追加したい、バージョンを変更したい場合は予めpipでインポートするライブラリモジュールを登録してください。<br>
仮想環境実行中ではyamlで定義した依存関係とインポートしたpipライブラリモジュールが使用しますが、仮想環境と関係なく元々インストールされているpipのライブラリモジュールも併用できます。

### 併用しているモジュール
- DeepL

### condaの仮想実行環境を作成
```
conda env create -f environment.yaml
```
### conda起動
```
conda activate ldm
```
### 起動失敗時は再度実行以下のコマンドを実行
```
conda init bash
```
### 初期化でも修復されない場合はyamlファイルで定義して作成した仮想環境を削除し、再作成を試す
```
rm -r /anaconda/envs/ldm
conda env create -f environment.yaml
conda activate ldm
```
### 起動に成功時に仮想環境でcudaが有効化されているか確認する
```
$ python3
Python 3.8.5 (default, Sep  4 2020, 07:30:14)
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> torch.version.cuda
>>> torch.cuda.is_available()

(True or False)
```
### Falseが出力された場合、cuda関連パッケージが入っているかを確認する
```
sudo apt list --installed | less
```

##　学習済みデータの導入
### データのclone(約4GBあるので長時間待機する)
```

git clone https://huggingface.co/CompVis/stable-diffusion-v-1-4-original
```
### 学習済みデータの確認
```
cd ~
du -h /diffusion-ai/stable-diffusion-v-1-4-original/sd-v1-4.ckpt
4.0G    stable-diffusion-v-1-4-original/sd-v1-4.ckpt　#4.0Gあれば問題なし。
```

### 学習済みデータセットを指定先にコピー
```
cd ~
mkdir /diffusion-ai/stable-diffusion/models/ldm/stable-diffusion-v1
cp -r ~/diffusion-ai/stable-diffusion-v-1-4-original/sd-v1-4.ckpt ~/diffusion-ai/stable-diffusion/models/ldm/stable-diffusion-v1/model.ckpt
```

## 画像生成テスト
### 画像生成用サンプルスクリプトを実行
```
cd ~/diffusion-ai/stable-diffusion/
python3 scripts/txt2img.py --prompt "a photograph of an astronaut riding a horse" --plms
```
### 生成画像出力先
```
ls ~/diffusion-ai/stable-diffusion/outputs/
```
<img src="https://lh3.googleusercontent.com/u/1/drive-viewer/AFDK6gN6WCAFiZJlQqiX7BJkKnSh3C-3-PTowsadp0FjBMF_SBxy8O0W7VYl9nv_jvPOyKdMP4_jOIv3EhZMM2UnRPHLec5nJw=w1467-h824" alt="馬に跨る宇宙飛行士">

## 作成したFast-APIの構成
```
~/fast-api$ ls
gen.sh  images  main.py  module  script
```

## 作成したFast-APIに学習済みデータをコピー
```
cp -r ~/diffusion-ai/stable-diffusion-v-1-4-original/sd-v1-4.ckpt ~/home/Azureユーザ名/fast-api/module/models/ldm/stable-diffusion-v1/
```
### main.pyを実行
main.pyでAPIを起動します。
クライアント側からリクエストに応じて
script/配下の`genimg.py`が実行され、画像パスをクライアントに、画像データをWebサーバに返します。
```
~/fast-api/script$ ls genimg.py
genimg.py
```
※Webサーバの画像を格納するパスのユーザ所有権がなかった場合
sudo chown th458-user imagesで画像をAIサーバからSCP出来るようになりました。

### AI画像生成APIリクエストのテスト
```
http://api_server_address:port/ai/debug/

{
    "user_id":"~~~~",
    "keyword":"美しい海,魚,たくさんの魚"
}
```
### レスポンスの確認
```
Respons Body(raw Json)
{
    "img_file": "~~~~.png"
}
Status 200 OK
```
## VM立ち上げ時の自動実行ファイルについて
VM起動時にgen.shがAPI自動起動。
```
~$ ls fast-api/gen.sh
fast-api/gen.sh
```
## gen.shの中身
```
#!/bin/sh
#source /anaconda/etc/profile.d/conda.sh
#conda activate ldm

#screen session
/usr/bin/sudo -u th458-user /usr/bin/screen -S api -X quit
/usr/bin/sudo -u th458-user /usr/bin/screen -dmS api
/usr/bin/sudo -u th458-user /usr/bin/screen -S api -X stuff 'cd /home/th458-user/fast-api\n'
/usr/bin/sudo -u th458-user /usr/bin/screen -S api -X stuff 'source /anaconda/etc/profile.d/conda.sh\n'
/usr/bin/sudo -u th458-user /usr/bin/screen -S api -X stuff 'conda activate ldm\n'
/usr/bin/sudo -u th458-user /usr/bin/screen -S api -X stuff 'python3 /home/th458-user/fast-api/main.py\n'
#python3 main.py
echo "finish"

```