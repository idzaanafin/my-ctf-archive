FROM node:latest

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

ENV flag=FLAG{test}
ENV secret=randomsecretvalue

EXPOSE 3000

CMD ["node", "bin/www"]