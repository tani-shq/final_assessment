# Use the official Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python application into the container
COPY app.py /app/app.py

# Expose the ports used by the application
EXPOSE 3000 3001

# Command to run the application
CMD ["python", "app.py"]
