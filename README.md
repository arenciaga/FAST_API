# Hiroto FastAPI Docker Demo

This is a minimal FastAPI web application designed as a demo or template for deployment with Docker. It serves as a "Hello Hiroto" example, likely for testing CI/CD pipelines, containerization, or orchestration workflows (referencing "Hiroto" in the code and instructions).

## Features
- **FastAPI** backend with two endpoints:
  - `GET /` : Returns a "Hello Hiroto" message along with filtered custom environment variables (excludes common system/AWS vars).
  - `GET /items/{item_id}` : Standard example endpoint with query param support.
- **Dockerized** for easy containerization and deployment.
- Includes `mangum` for potential AWS Lambda compatibility via ASGI adapter.
- Interactive API docs available at `/docs` (Swagger UI).

## Project Structure
```
.
├── app/
│   └── main.py          # Main FastAPI application
├── Dockerfile
├── requirements.txt
├── LICENSE
└── README.md
```

## Setup & Run Locally

### Prerequisites
- Python 3.8+
- Docker (recommended)

### Using Docker (Recommended)
```bash
# Build the image
docker build -t hiroto-fastapi .

# Run the container
docker run -p 8080:80 hiroto-fastapi

# Access the app
# - API: http://localhost:8080
# - Interactive docs: http://localhost:8080/docs
```

### Without Docker (Development)
```bash
# Install dependencies
pip install -r requirements.txt

# Run with uvicorn
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## Endpoints
- `GET /` - Hello message + env vars
- `GET /items/{item_id}?q=optional` - Item retrieval example
- `GET /docs` - Swagger UI
- `GET /redoc` - ReDoc UI

## Environment Variables
The root endpoint filters and exposes non-system environment variables for debugging/deployment inspection.

## License
MIT License (see LICENSE file). Original copyright by Ranoarison Rajoniaina (2022), adapted for Hiroto demo.