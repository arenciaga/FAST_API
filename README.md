# FastAPI Docker Demo

This codebase is a minimal, clean **FastAPI** web application that demonstrates best practices for building containerized Python APIs. It serves as an excellent starting point or template for microservices, serverless functions, or learning FastAPI.

- Simple REST API with two endpoints (root + parameterized item)
- Secure environment variable inspection (filters noisy/system vars)
- Full Docker containerization (Python 3.8 base, runs on port 80)
- Serverless readiness (includes Mangum adapter for AWS Lambda)

## What the App Does

The application exposes a FastAPI server that:

- **GET /** — Returns a greeting along with a filtered dictionary of the current environment variables (excludes common system, Python, and cloud provider vars like AWS_*, PATH, etc.). Useful for safely debugging deployments in containers or serverless environments.
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

**Key Features & Best Practices Demonstrated**:
- Auto-generated interactive docs (Swagger UI at `/docs`, ReDoc at `/redoc`)
- Clean dependency management and minimal base image
- Environment filtering to prevent leaking secrets or clutter
- Compatibility with both Docker and serverless (via Mangum)
- Production-oriented setup (non-root port binding, uvicorn ASGI server)

The greeting "Hello Hiroto" is a placeholder that can be customized for your project or team.