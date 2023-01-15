FROM node:16.18.0-alpine3.16 AS build
COPY ./app/package*.json ./
RUN npm ci
ARG VITE_API_SERVER
ARG VITE_TOKEN_KEY
COPY ./app/ .
RUN npm run build


FROM nginx:1.14.1

# 開発ディレクトリ設定
ENV WORKDIR /usr/share/nginx/html/
WORKDIR ${WORKDIR}

RUN mkdir /usr/share/nginx/html/static
RUN mkdir /usr/share/nginx/html/media
RUN mkdir /usr/share/nginx/html/locales
COPY --from=build dist /usr/share/nginx/html
a
