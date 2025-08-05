# Use official Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /code

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    netcat-openbsd \
    && apt-get clean

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . .

# Make the entrypoint script executable
RUN chmod +x /code/entrypoint.sh

# Specify the entrypoint script
ENTRYPOINT ["/code/entrypoint.sh"]

# Default command to run
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
