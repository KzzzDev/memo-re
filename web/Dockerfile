FROM node:16.18.0-alpine3.16 AS build
COPY ./app/package*.json .
RUN npm ci
COPY ./app/ .
RUN npm run build

FROM nginx:1.14.1
RUN mkdir /usr/share/nginx/html/static
RUN mkdir /usr/share/nginx/html/media
COPY --from=build dist /usr/share/nginx/html/static