from app.api.predict import router as predict_router
from fastapi import FastAPI

app = FastAPI(
    title="Dhaka Property Price Predictor API",
    description="Production-grade REST API for predicting apartment and property prices in Dhaka, Bangladesh.",
    version="1.0.0",
)

app.include_router(predict_router, prefix="/api/v1", tags=["Prediction"])


@app.get("/")
def root():
    return {
        "status": "online",
        "message": "Dhaka Property Price Predictor API is running.",
        "interactive_docs": "/docs",
    }