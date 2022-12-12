FROM node:16.13

# 開発ディレクトリ設定
ENV WORKDIR /code
WORKDIR ${WORKDIR}
COPY ./scripts/ ${WORKDIR}/
COPY ./app/ ${WORKDIR}/app/

# コンテナ内でパッケージを一括インストール
RUN cd app && npm update npm && npm ci
