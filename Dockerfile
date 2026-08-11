# Use an official Python runtime as a parent image
FROM python:3.13-slim

# Create system group and system user, 
#'--system' means no login shell and no home directory
# '--create-home' gives the home directory to the user
RUN groupadd --system appgroup && useradd --create-home appuser

# Set the working directory in the container
WORKDIR /src

# Copy the requirement file into the container directory at .
COPY requirements.txt .

# Install needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container directory at .
COPY ./app ./app

# Copy the current directory contents into the container directory at .
COPY ./envs ./envs

# Copy the current directory contents into the container directory at .
COPY ./tests/integrations ./tests

# Copy the current directory contents into the container directory at .
COPY ./tests/integrations ./tests

# Copy the current directory contents into the container directory at .
COPY ./tests/__init__.py ./tests

# Copy the current directory contents into the container directory at .
COPY ./tests/conftest.py ./tests

# Copy the current directory contents into the container directory at .
COPY pyproject.toml ./app

# Ensure the app user owns the working directory
RUN chown -R appuser:appgroup ./src

# Make port 80 available to the world outside this container
EXPOSE 8000

# Switch all subsequence instructions and the runtime proces to the user
USER appuser

# Run app.py when the container launches
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
