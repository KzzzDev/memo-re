FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
EXPOSE 8000

# 開発ディレクトリ設定
ENV WORKDIR /usr/src/app
WORKDIR ${WORKDIR}
COPY start.sh ${WORKDIR}/

# コンテナ内でパッケージを一括インストール
COPY requirements.txt ${WORKDIR}
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install coreapi django-cors-headers python-jose

COPY ./app/ ${WORKDIR}/
# media/だけコピーされないので追記
COPY ./app/media/ ${WORKDIR}/app/media/
