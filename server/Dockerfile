# Grab Python 3.x image
FROM python:3

# Let Python output be sent to the host computer
ENV PYTHONUNBUFFERED 1

# Define/create a working directory for the RUN/CMD/COPY commands
WORKDIR /app

# Copy the contents of the "src" folder to the container
COPY ./src .

# Install the required dependencies
RUN pip install -r requirements.txt

# Tell Docker to listen to traffic on this port inside the container
EXPOSE 6543

# Start the Pyramid web server
CMD ["python", "rest-server.py"]
