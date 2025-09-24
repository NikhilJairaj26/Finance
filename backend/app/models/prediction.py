from pydantic import BaseModel
from typing import List, Dict

class PredictionInput(BaseModel):
    # Define the input fields for your ML model
    # This is an example, adjust it to your model's needs
    age: int
    income: float
    # ... other features

class PredictionOutput(BaseModel):
    prediction: float

class SavingsAdvice(BaseModel):
    advice: str
    # You can add more fields like charts data, etc.

class InvestmentRecommendation(BaseModel):
    recommendations: List[Dict[str, str]] # e.g. [{"stock": "AAPL", "reason": "..."}]
