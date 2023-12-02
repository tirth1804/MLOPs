# Use the official Python image as a base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 80 to the outside world
EXPOSE 80

# Set environment variable
ENV NAME World

# Define the command to run your application
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:app"]
