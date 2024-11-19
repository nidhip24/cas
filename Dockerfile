# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the project files to the working directory
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install -r requirements.txt
RUN pip install --no-cache-dir --force-reinstall uvicorn

# Expose the application port
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
