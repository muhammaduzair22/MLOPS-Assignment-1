# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /MLOPS-Assignment-1

# Copy the current directory contents into the container at /app
COPY . /MLOPS-Assignment-1

# Install any needed packages specified in requirements.txt
# Make sure Flask is included in your requirements.txt
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run model.py when the container launches
CMD ["python", "train_model.py"]
