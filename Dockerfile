# Use Python base image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port 5000
EXPOSE 5000

# Set environment variable for Flask
ENV FLASK_APP=flask_app.py

# Run the application
CMD ["flask", "run", "--host=0.0.0.0"]
