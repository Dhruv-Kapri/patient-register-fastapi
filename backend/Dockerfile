# base image
FROM Python:3.11-slim

# Prevent Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .

# Copy the rest of application code
COPY . .

# Expose application port
EXPOSE 8000

# command to start FastAPI application
CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000" ]