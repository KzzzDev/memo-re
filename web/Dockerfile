FROM node:16.18.0-alpine3.16 AS build
COPY ./app/package*.json .
RUN npm ci
COPY ./app/ .
RUN npm run build


FROM nginx:1.14.1

# 開発ディレクトリ設定
ENV WORKDIR /usr/share/nginx/
WORKDIR ${WORKDIR}

RUN mkdir /usr/share/nginx/html/static
RUN mkdir /usr/share/nginx/html/static/assets
RUN mkdir /usr/share/nginx/html/static/locales
RUN mkdir /usr/share/nginx/html/media
COPY --from=build dist/index.html /usr/share/nginx/html
COPY --from=build dist/assets /usr/share/nginx/html/static/assets
COPY --from=build dist/locales /usr/share/nginx/html/static/locales