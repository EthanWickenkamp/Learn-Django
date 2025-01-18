# Use the Node.js image for development
FROM node:18

# Set working directory inside the container
WORKDIR /app

# Copy only package.json and package-lock.json to install dependencies first
COPY learn/package*.json  learn/package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application files
COPY . .

# Expose the port for the Svelte dev server
EXPOSE 5173

# Default command to run the development server
#CMD ["npm", "run", "dev"]