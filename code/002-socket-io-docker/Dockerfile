FROM node:16

COPY package*.json ./
RUN npm install
COPY index.js index.js
COPY index.html index.html

CMD [ "node", "index.js" ]
