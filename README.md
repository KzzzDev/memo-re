# memo:Re

<div align="center">
    <img src="./docs/logo.svg" alt="Lighthouse logo" height="210" style="display: block">
    <span style="font-weight: bold">memo:R</span>
</div>

## インストール

```sh
git clone https://github.com/Kazumasa1/memo-re.git
```

## 使い方

次のコマンドを実行してDocker コンテナを構築します。

```bash
cd memo-re
docker-compose build --no-cache
docker rmi $(docker images --filter "dangling=true" -q)
docker-compose up -d
```

## 動作環境

- Nginx(Django): http://localhost:8000

### ディレクトリ構成

```sh
memo-re
├─── README.md
├─── back
│   ├─── app                    # Djangoのプロジェクト
│   │   ├─── api
│   │   │   └─── migrations
│   │   ├─── config
│   │   └─── templates
│   └─── scripts                # docker-compose up で実行される Django起動シェル
├─── db
└─── web
    ├─── app                    # Vueのプロジェクト
    │   ├─── component
    │   ├─── lib
    │   ├─── plugin
    │   ├─── public
    │   │   └─── locales
    │   └─── views
    │       ├─── brain
    │       ├─── friend
    │       └─── user
    └─── conf
```

## 作者

- [@Kazumasa1](https://github.com/Kazumasa1)
- [@KleinChiu](https://github.com/KleinChiu)
- [@SoraUno](https://github.com/SoraUno)
- [@Yuuma-ujimoto](https://github.com/Yuuma-ujimoto)
- [@honjii](https://github.com/honjii)
- [@mi1207](https://github.com/mi1207)
- [@nagi-lc3](https://github.com/nagi-lc3)
- [@reone19](https://github.com/reone19)
- [@sean-dp](https://github.com/sean-dp)
