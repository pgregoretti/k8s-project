from fastapi import FastAPI
import socket, os, logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)

@app.get("/")
def root():
    logging.info("Root endpoint hit")
    return {"message": "Hello from Kubernetes project"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/info")
def info():
    return {
        "hostname": socket.gethostname(),
        "env": os.getenv("ENV", "dev")
    }

@app.get("/config")
def config():
    return {
        "env": os.getenv("ENV", "dev"),
        "version": os.getenv("VERSION", "1.0")
    }