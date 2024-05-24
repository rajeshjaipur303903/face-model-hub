# Dockerfile
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the Python script into the container
COPY fetch_top_models.py /app/fetch_top_models.py

# Install the required Python packages
RUN pip install requests

# Run the Python script
CMD ["python", "fetch_top_models.py"]