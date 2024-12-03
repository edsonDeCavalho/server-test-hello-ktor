# Use an official Python image as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir flask

# Expose port 5000 for the Flask app
EXPOSE 8089

# Define the command to run the application
CMD ["python", "app.py"]
