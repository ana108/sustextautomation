# Use a lightweight Python base image
#FROM mcr.microsoft.com/playwright/python:v1.50.0-noble
FROM python:3.12-bookworm
# Set the working directory inside the container
WORKDIR /SustainableTextAutomation

# Copy the requirements file and install dependencies

# Copy the application source code
COPY automation automation
COPY requirements.txt .

RUN pip install -r requirements.txt && \
    playwright install --with-deps

# Expose the port the application listens on
RUN cd automation

# Define the command to run the application when the container starts
CMD ["pytest"]