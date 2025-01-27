FROM node:18

WORKDIR /app

COPY learn/package*.json  learn/package-lock.json ./
RUN npm install

COPY . .

EXPOSE 5173

#CMD ["npm", "run", "dev"]