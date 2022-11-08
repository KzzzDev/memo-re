FROM 16.18.0-alpine3.16 AS build
COPY package*.json .
RUN npm ci
RUN npm run build
# COPY --from=build static