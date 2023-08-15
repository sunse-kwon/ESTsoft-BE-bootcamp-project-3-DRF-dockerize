FROM nginx:stable-alpine3.17-slim

EXPOSE 80

COPY ./default.conf /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]