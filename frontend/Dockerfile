# frontend/Dockerfile
FROM node:14-alpine AS build

WORKDIR /app

COPY . .

RUN npm install

RUN npm run build

FROM nginx:alpine

COPY --from=build /app/build /usr/share/nginx/html

COPY nginx.conf /etc/nginx/nginx.d

CMD ["nginx", "-g", "daemon off;"]