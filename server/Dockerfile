# Simple Node image for the API server
FROM node:18-alpine

WORKDIR /usr/src/app

# Copy only package manifest first (if you later add package.json)
# but for this lab we install minimal deps directly
RUN npm init -y && npm install express mongoose cors

# Copy app code
COPY app.js ./
COPY database ./database

EXPOSE 3030
CMD ["node", "app.js"]
