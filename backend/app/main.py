from fastapi import FastAPI

app = FastAPI(
    title="DesignForge AI",
    description="AI Software Architect",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to DesignForge AI"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }