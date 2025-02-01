# Use a lightweight Python base image
FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

ADD . /app


# Copy requirements.txt to the container
COPY requirements.txt /app/requirements.txt


# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb-dev \
    libmariadb-dev-compat \
    pkg-config \
    && apt-get clean
# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code
COPY . /app

