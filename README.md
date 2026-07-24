# 🏢 Dhaka Property Price Predictor API

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-green.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An end-to-end Machine Learning REST API that predicts apartment and property prices in Dhaka, Bangladesh (in BDT). Built with **FastAPI**, **Scikit-Learn (Random Forest Regressor)**, and containerized using **Docker**.

---

## 📊 Model Performance

| Metric | Score / Detail |
| :--- | :--- |
| **Algorithm** | Random Forest Regressor |
| **Training $R^2$** | `0.9791` |
| **Testing $R^2$** | `0.8714` |
| **Primary Features** | Area (sq ft), Bedrooms, Bathrooms, Location |

---

## 🛠️ Tech Stack & Architecture

* **Machine Learning:** Pandas, Scikit-Learn (`ColumnTransformer`, `OneHotEncoder`, `StandardScaler`, `RandomForestRegressor`), Joblib.
* **Backend Framework:** FastAPI, Pydantic v2, Uvicorn.
* **Testing & Containerization:** Pytest, HTTPX, Docker.

---

## 🚀 How to Run Locally

### 1. Clone the Repository & Set Up Virtual Environment

```bash
git clone [https://github.com/rafatistiak/dhaka-property-price-predictor.git](https://github.com/rafatistiak/dhaka-property-price-predictor.git)
cd dhaka-property-price-predictor

python -m venv venv
# On Windows PowerShell:
.\venv\Scripts\Activate.ps1

pip install -r requirements.txt
