# Use the official Python 3.9 slim base image
FROM python:3.9-slim

# Copy only the requirements file to the container
COPY requirements.txt /app/

# Set the working directory inside the container to /app
WORKDIR /app

# Install Python dependencies specified in requirements.txt
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# COPY the rest of the application code to the container
COPY . /app

# Define the command to run python when the container starts
CMD ["python", "hello.py"]
