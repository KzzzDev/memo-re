FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
EXPOSE 8000

# 開発ディレクトリ設定
ENV WORKDIR /usr/src
# ENV WORKDIR /usr/src/app
WORKDIR ${WORKDIR}
COPY ./scripts/ ${WORKDIR}/

# コンテナ内でパッケージを一括インストール
COPY requirements.txt ${WORKDIR}
RUN pip install --upgrade pip && pip install -r requirements.txt && \
    pip install coreapi django-cors-headers python-jose

COPY . ${WORKDIR}/