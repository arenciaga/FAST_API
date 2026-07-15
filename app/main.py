import os
from typing import Union

from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Hello World",
    description="A simple Dockerized FastAPI app that greets 'Hello Hiroto' and exposes environment variables for debugging.",
    version="1.0.0",
)


@app.get("/", summary="Root endpoint", description="Returns a greeting and filtered environment variables (excluding sensitive/system ones).")
def read_root():
    """Root endpoint that demonstrates environment variable access in a containerized environment.

    Filters out common system, AWS, Lambda, and Python runtime variables to show only custom/user-defined ones.
    Useful for cloud deployments (ECS, Lambda, Kubernetes) where you want to inspect injected config.
    """
    # Filter to show only custom vars (exclude AWS_, Lambda_, PATH, Python internals, etc.)
    custom_vars = {
        key: value
        for key, value in os.environ.items()
        if not key.startswith(
            ("AWS_", "LAMBDA_", "PATH", "_", "LD_", "PYTHON", "TZ", "SHLVL", "LANG", "LC_", "PWD")
        )
    }
    return {
        "message": "Hello Hiroto",
        "env_vars": custom_vars,
    }


@app.get(
    "/items/{item_id}",
    summary="Get item",
    description="Example endpoint demonstrating path and query parameters.",
)
def read_item(item_id: int, q: Union[str, None] = None):
    """Example endpoint that echoes back the path parameter and optional query string.

    This follows the FastAPI tutorial pattern and shows type validation (int for item_id).
    """
    return {"item_id": item_id, "q": q}

