# Use Python official image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy all files into container
COPY . .

# Install Flask
RUN pip install flask

# Expose port
EXPOSE 8080

# Run the app
CMD ["python", "app.py"]
