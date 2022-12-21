# memo:Re

## インストール

```sh
git clone https://github.com/Kazumasa1/memo-re.git
```

## envの設定
- ”.env.sample" を ".env"に変更してコードを書き加えてください。

## 使い方

次のコマンドを実行してDocker コンテナを構築します。

```bash
cd memo-re
docker-compose build --no-cache
docker-compose up -d
docker-compose restart back
```

## 動作環境

- Nginx(Django): http://localhost:8000

- Nginx(Django)管理者サイト: http://localhost:8000/admin
  - メールアドレス: admin@example.com
  - パスワード: admin

- Nginx(Django)APIドキュメントダウンロード: http://localhost:8000/api/schema/

- Nginx(Django)APIドキュメント:swaggerUIで閲覧およびテスト http://localhost:8000/api/schema/swagger-ui/

- Nginx(Django)APIドキュメント:redocで閲覧およびテスト http://localhost:8000/api/schema/redoc/

### ディレクトリ構成

```sh
memo-re
├── README.md
├── back
│   ├── Dockerfile
│   ├── app			# Djangoのプロジェクト
│   ├── requirements.txt
│   ├── start.sh	# docker-compose up で実行される Django起動シェル
│   └── templates
├── db
│   ├── Dockerfile
│   └── my.cnf
├── docker-compose.yml
└── web
    ├── Dockerfile
    ├── app			# Vueのプロジェクト
    ├── conf
    ├── logs
    └── uwsgi_params
```

### システム構成図

<img src="./docs/system.png" alt="memo:Re logo" width="550">

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

---

<div align="center">
    <img src="./docs/logo.svg" alt="memo:Re logo" height="210" style="display: block">
    <p style="font-weight: bold">memo:Re</p>
</div>
