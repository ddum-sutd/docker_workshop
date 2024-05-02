# Use the official Python 3.9 slim base image
FROM python:3.9-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Add the contents of current directory (.) into the container's /app directory
ADD . /app

# Install Python dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define the command to run python when the container starts
CMD ["python", "hello.py"]
