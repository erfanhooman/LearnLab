# Use the official Python image as base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script from the host machine into the container
COPY . /app/

# Install any dependencies your script might have
# If you have a requirements.txt file, uncomment the following line
COPY requirements.txt /app/
# RUN pip install --no-cache-dir -r requirements.txt

# Run the Python script when the container starts
CMD ["python", "your_script.py"]