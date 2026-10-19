import logging

from fastapi import FastAPI

logger = logging.getLogger(__name__)


app = FastAPI(title="group-pay")


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/health")
def health():
    return {"status": "healthy"}
