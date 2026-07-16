import os
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

# Root endpoint that returns a greeting and filtered environment variables
# Useful for debugging deployments (containers, AWS Lambda, etc.)
@app.get("/")
def read_root():
    # Filter out common system, Python, and cloud provider env vars to avoid noise/secrets
    custom_vars = {
        key: value for key, value in os.environ.items()
        if not key.startswith(("AWS_", "LAMBDA_", "PATH", "_", "LD_", "PYTHON", "TZ", "SHLVL", "LANG", "LC_", "PWD"))
    }
    return {
        "message": "Hello Hiroto",
        "env_vars": custom_vars,
    }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
