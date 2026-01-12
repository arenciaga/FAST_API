import os
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    # Return all environment variables (for testing)
    env_vars = {key: value for key, value in os.environ.items()}
    return {
        "message": "Environment Variables Test",
        "env_vars": env_vars,
    }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
