from pathlib import Path
import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# 1. Locate dataset relative to this script
BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "property_data.csv"

print(f"Loading data from {CSV_PATH}...")
df = pd.read_csv(CSV_PATH)

# 2. Map actual CSV columns from your Kaggle dataset
# CSV columns: ['Location', 'Price', 'No. Beds', 'No. Baths', 'Area']
raw_cols = ["Area", "No. Beds", "No. Baths", "Location", "Price"]

# Drop missing values in these key columns
df = df.dropna(subset=raw_cols)

# Clean numeric values if needed (convert strings to numbers)
df["Area"] = pd.to_numeric(df["Area"], errors="coerce")
df["No. Beds"] = pd.to_numeric(df["No. Beds"], errors="coerce")
df["No. Baths"] = pd.to_numeric(df["No. Baths"], errors="coerce")
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

df = df.dropna(subset=raw_cols)

# Rename to standardized names for our API pipeline
df = df.rename(
    columns={
        "Area": "area_sqft",
        "No. Beds": "bedrooms",
        "No. Baths": "bathrooms",
        "Location": "location",
        "Price": "price_bdt",
    }
)

X = df[["area_sqft", "bedrooms", "bathrooms", "location"]]
y = df["price_bdt"]

# 3. Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Preprocessing Pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), ["area_sqft", "bedrooms", "bathrooms"]),
        ("cat", OneHotEncoder(handle_unknown="ignore"), ["location"]),
    ]
)

# 5. Connect Preprocessing + Random Forest Regressor
pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("regressor", RandomForestRegressor(n_estimators=100, random_state=42)),
    ]
)

print("Training Random Forest Regressor model...")
pipeline.fit(X_train, y_train)

# 6. Evaluate and Save Artifact
train_score = pipeline.score(X_train, y_train)
test_score = pipeline.score(X_test, y_test)
print(f"Model Training R² Score: {train_score:.4f}")
print(f"Model Testing R² Score:  {test_score:.4f}")

artifact_path = BASE_DIR.parent / "artifacts" / "dhaka_model.joblib"
joblib.dump(pipeline, artifact_path)
print(f"✅ Success! Trained model saved to: {artifact_path}")