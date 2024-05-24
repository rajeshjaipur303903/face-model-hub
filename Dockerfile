# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install requests

# Make run_cron.sh executable
RUN chmod +x run_cron.sh

# Run the shell script that sets up and starts the cron job
CMD ["./run_cron.sh"]


