FROM node:16.13

# 開発ディレクトリ設定
ENV WORKDIR /code
WORKDIR ${WORKDIR}
COPY ./scripts/ ${WORKDIR}/

# コンテナ内でパッケージを一括インストール
RUN npm update npm && npm install -g @vue/cli && \
    npm install -g @vue/cli@5.0.4

COPY . ${WORKDIR}/