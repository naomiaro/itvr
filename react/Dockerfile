FROM node:14

WORKDIR /web

COPY package*.json /web/
RUN npm install && npm cache clean --force

COPY . .

EXPOSE 3000
