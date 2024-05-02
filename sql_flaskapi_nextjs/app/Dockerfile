# Use the official Python image as a base
FROM python:3.6

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install Flask and MySQL Connector Python
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]
