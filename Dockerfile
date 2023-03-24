# Set the base image
FROM python:latest

# Set the working directory
WORKDIR /app


COPY requirements.txt .

RUN pip install -r requirements.txt

# Copy the application code into the container
COPY init.py .
COPY model/ model/

# Expose the port that the application will be running on
EXPOSE 5000

# Start the application
CMD ["python", "init.py"]
