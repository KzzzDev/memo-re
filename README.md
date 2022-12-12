# memo:Re
味噌展プロジェクト

## Installation

```bash
git clone https://github.com/Kazumasa1/memo-re.git
```

## Requirement

### ディレクトリ構成

```bash
memo-re
├── README.md
├── back
│   ├── Dockerfile
│   ├── app  # ← Djangoのプロジェクト
│   │   ├── api
│   │   ├── config
│   │   ├── manage.py
│   │   ├── media
│   │   ├── static
│   │   └── templates
│   ├── media
│   ├── requirements.txt
│   ├── scripts
│   │   └── start.sh  # ← docker-compose up で実行される Django起動シェル
│   └── static
├── db
│   ├── Dockerfile
│   └── my.cnf
├── docker-compose.yml
├── front
│   ├── Dockerfile
│   ├── app  # ← Vueのプロジェクト
│   │   ├── App.vue
│   │   ├── README.md
│   │   ├── component
│   │   ├── dist  # ← docker-compose build 後に生成されるディレクトリ
│   │   ├── env.d.ts
│   │   ├── index.html
│   │   ├── lib
│   │   ├── main.ts
│   │   ├── node_modules
│   │   ├── package-lock.json
│   │   ├── package.json
│   │   ├── plugin
│   │   ├── public
│   │   ├── tsconfig.json
│   │   ├── tsconfig.node.json
│   │   ├── views
│   │   └── vite.config.ts
│   └── scripts
│       └── start.sh  # ← docker-compose up で実行される Vue起動シェル
└── web
    ├── Dockerfile
    ├── conf
    │   └── app_nginx.conf
    ├── logs
    │   └── nginx
    └── uwsgi_params
```
### Notice

フロントの方でVueのプロジェクトを変更する際は```memo-re/front/```の```app```ディレクトリを変更してください。現状では、そのまま入れ替えてもらって大丈夫です。

## Usage

### Set up

次のコマンドを実行してDocker コンテナを構築します。

```bash
cd memo-re
docker-compose build --no-cache
docker rmi $(docker images --filter "dangling=true" -q)
docker-compose up -d
```

### Memo

- Nginx(Django): http://localhost:8000
- Vue: http://localhost:8080 or http://localhost:5173

## Author

- [@Kazumasa1](https://github.com/Kazumasa1)
- [@KleinChiu](https://github.com/KleinChiu)
- [@SoraUno](https://github.com/SoraUno)
- [@Yuuma-ujimoto](https://github.com/Yuuma-ujimoto)
- [@honjii](https://github.com/honjii)
- [@mi1207](https://github.com/mi1207)
- [@nagi-lc3](https://github.com/nagi-lc3)
- [@reone19](https://github.com/reone19)
- [@sean-dp](https://github.com/sean-dp)
