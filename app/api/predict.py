from pathlib import Path
import joblib
import pandas as pd
from app.schemas.property import PropertyRequest, PropertyResponse
from fastapi import APIRouter, HTTPException

router = APIRouter()

# Load model artifact once on startup
BASE_DIR = Path(__file__).resolve().parent.parent.parent
MODEL_PATH = BASE_DIR / "artifacts" / "dhaka_model.joblib"

if not MODEL_PATH.exists():
    raise FileNotFoundError(f"Model artifact not found at {MODEL_PATH}")

model = joblib.load(MODEL_PATH)


@router.post("/predict", response_model=PropertyResponse)
def predict_property_price(payload: PropertyRequest):
    try:
        # Convert request body into DataFrame matching model features
        input_data = pd.DataFrame(
            [
                {
                    "area_sqft": payload.area_sqft,
                    "bedrooms": payload.bedrooms,
                    "bathrooms": payload.bathrooms,
                    "location": payload.location,
                }
            ]
        )

        # Run inference using saved model pipeline
        raw_price = model.predict(input_data)[0]
        price_bdt = round(float(raw_price), 2)
        price_per_sqft = round(price_bdt / payload.area_sqft, 2)

        return PropertyResponse(
            estimated_price_bdt=price_bdt,
            formatted_price=f"৳ {price_bdt:,.2f}",
            price_per_sqft=price_per_sqft,
        )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Prediction Engine Error: {str(e)}"
        )