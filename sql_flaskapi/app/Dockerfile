# Use the official Python image as a base
FROM python:3.6

# Copy only the requirements file to the container
COPY requirements.txt /app/

# Set the working directory in the container
WORKDIR /app

# Install Python dependencies specified in requirements.txt
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# COPY the rest of the application code to the container
COPY . /app

# Expose port 5000
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]
