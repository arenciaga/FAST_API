FROM python:3.8-slim

# Set working directory for the container
WORKDIR /code

# Copy and install Python dependencies first (better layer caching)
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy application code
COPY ./app /code/app

# Run the FastAPI app with Uvicorn on port 80
# --host 0.0.0.0 allows access from outside the container
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
