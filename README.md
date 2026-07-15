# FastAPI Dockerized App

This is a simple **Hello World** web application built with [FastAPI](https://fastapi.tiangolo.com/) and containerized using Docker.

## What it does

- Exposes a REST API with two endpoints:
  - `GET /` — Returns a greeting message "Hello Hiroto" along with a filtered list of non-sensitive environment variables (useful for debugging in container/cloud environments).
  - `GET /items/{item_id}` — Example endpoint that returns the provided `item_id` and optional query parameter `q`.
- The app is designed to run efficiently in a Docker container.
- Includes interactive API documentation at `/docs` (Swagger UI) and `/redoc`.

## How to build and run

### 1. Build the Docker image
```bash
docker build -t fastapi-app .
```

### 2. Run the container
```bash
docker run -p 8080:80 fastapi-app
```

The app will be available at:
- http://localhost:8080
- http://localhost:8080/docs (Interactive Swagger UI)
- http://localhost:8080/redoc (Alternative docs)

### Environment Variables
The root endpoint (`/`) filters and displays custom environment variables (excluding AWS, Lambda, Python internals, etc.) to help with cloud/container debugging.

## Project Structure
```
.
├── app/
│   └── main.py          # FastAPI application code
├── Dockerfile           # Docker configuration
├── requirements.txt     # Python dependencies
├── README.md
└── LICENSE
```

## Tech Stack
- **FastAPI**: Modern, fast (high-performance) Python web framework.
- **Uvicorn**: ASGI server to run the app.
- **Docker**: Containerization for easy deployment.

This project serves as a minimal, production-ready template for FastAPI apps that can be deployed to containers, AWS Lambda (via Mangum), or cloud platforms.