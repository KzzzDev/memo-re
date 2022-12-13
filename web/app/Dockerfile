FROM node:16.18.0-alpine3.16 AS build
COPY package*.json .
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:1.23.2-alpine
COPY --from=build dist /usr/share/nginx/html
