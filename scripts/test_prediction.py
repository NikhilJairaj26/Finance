import os
import sys
import pandas as pd
from pydantic import BaseModel

# Add the backend directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))

from app.ml.expense_predictor import ExpensePredictor

class PredictionInput(BaseModel):
    age: int
    income: float

def test_prediction():
    print("Testing expense prediction...")
    predictor = ExpensePredictor()
    
    # Sample input data
    sample_input = PredictionInput(age=30, income=5000)
    
    prediction = predictor.predict(sample_input)
    print(f"Sample prediction for income={sample_input.income}, age={sample_input.age}: ${prediction:.2f}")
    
    if prediction > 0:
        print("Prediction successful and value is positive.")
    else:
        print("Prediction might be incorrect or negative.")

if __name__ == "__main__":
    test_prediction()
