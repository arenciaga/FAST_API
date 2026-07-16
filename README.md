# FastAPI Docker Demo

This codebase is a minimal, production-ready **FastAPI** web application that demonstrates:

- A simple REST API with two endpoints
- Environment variable inspection (filters out common system/AWS vars)
- Containerization with **Docker**
- Deployment readiness (designed to run on port 80, compatible with AWS Lambda via Mangum, etc.)

## What the App Does

The application exposes a FastAPI server that:

- **GET /** — Returns a greeting "Hello" along with a filtered dictionary of the current environment variables. This is useful for debugging cloud/container environments without exposing secrets or noisy system variables.
- **GET /items/{item_id}** — Standard FastAPI example endpoint that accepts an `item_id` path parameter and an optional `q` query parameter.

It also includes:
- Interactive API documentation at `/docs` (Swagger UI) and `/redoc`
- Dependencies managed via `requirements.txt` (FastAPI, Uvicorn, Mangum for serverless)
- A `Dockerfile` based on Python 3.8 that installs dependencies and runs the app on port 80

## Quick Start

### With Docker (recommended)

```bash
# Build the image
docker build -t fastapi-docker-demo .

# Run the container
docker run -p 8080:80 fastapi-docker-demo
```

Then visit:
- http://localhost:8080/ 
- http://localhost:8080/docs (interactive Swagger UI)

### Locally (without Docker)

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Project Structure

```
.
├── app/
│   └── main.py          # Main FastAPI application
├── Dockerfile           # Container definition
├── requirements.txt     # Python dependencies
├── README.md
└── LICENSE
```

This is a lightweight template ideal for learning FastAPI, testing containerized Python web services, or as a starting point for microservices and serverless APIs.

**Note**: The greeting has been updated to a simple "Hello" by Grok.