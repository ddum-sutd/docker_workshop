# Use the official Node.js 18 image as the base
FROM node:18

# Copy the package.json and package-lock.json files to the container
COPY package*.json /app/

# Install project dependencies
RUN npm install

# Set the working directory inside the container
WORKDIR /app

# Copy the entire project to the container
COPY . /app

# Build the Next.js application
RUN npm run build

# Expose the desired port (change it to the appropriate port number if needed)
EXPOSE 3000

# Start the Next.js application
CMD [ "npm", "start" ]
