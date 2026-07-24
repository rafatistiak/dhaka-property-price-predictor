from pydantic import BaseModel, Field


class PropertyRequest(BaseModel):
    area_sqft: float = Field(
        ...,
        gt=100,
        lt=20000,
        example=1350.0,
        description="Property area in square feet",
    )
    bedrooms: int = Field(
        ..., ge=1, le=10, example=3, description="Number of bedrooms"
    )
    bathrooms: int = Field(
        ..., ge=1, le=10, example=3, description="Number of bathrooms"
    )
    location: str = Field(
        ..., example="Uttara", description="Location/neighborhood in Dhaka"
    )


class PropertyResponse(BaseModel):
    estimated_price_bdt: float
    formatted_price: str
    price_per_sqft: float
    status: str = "success"