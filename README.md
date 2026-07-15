# FastAPI Docker App
Sample FastAPI "Hello Hiroto" app with Dockerfile that exposes (filtered) environment variables.
## Build and Run
```bash
# Build
docker build -t my_fastapi_app .
# Run
docker run -p 80:80 my_fastapi_app
```

The app serves at `http://0.0.0.0:80` with Swagger at `/docs`.

The root endpoint returns "Hello Hiroto" along with filtered environment variables (excluding common system, AWS, and runtime vars).