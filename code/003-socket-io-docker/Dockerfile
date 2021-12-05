FROM node:16
COPY index.html index.html
COPY index.js index.js
COPY package-lock.json package-lock.json
COPY package.json package.json

RUN npm install

CMD [ "node", "index.js" ]