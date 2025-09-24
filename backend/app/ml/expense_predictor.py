import os
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib

class ExpensePredictor:
    def __init__(self, model_path=None):
        if model_path is None:
            # Construct absolute path to model file
            script_dir = os.path.dirname(os.path.abspath(__file__))
            self.model_path = os.path.join(script_dir, '..', '..', '..', 'data', 'models', 'expense_predictor.pkl')
        else:
            self.model_path = model_path
        self.model = None
        self.features = None # Initialize features

    def train(self, data_path=None):
        if data_path is None:
            # Construct absolute path to training data
            script_dir = os.path.dirname(os.path.abspath(__file__))
            data_path = os.path.join(script_dir, '..', '..', '..', 'data', 'training_data.csv')

        df = pd.read_csv(data_path)
        # Preprocessing and feature engineering
        # This is a simplified example
        self.features = ['income', 'age'] # Store features
        target = 'amount'
        # Drop rows with NaN values in the features
        df.dropna(subset=self.features, inplace=True)

        X = df[self.features]
        y = df[target]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)

        # Evaluate the model
        print(f"Model accuracy: {self.model.score(X_test, y_test)}")

        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(self.model_path), exist_ok=True)

        # Save the model
        joblib.dump(self.model, self.model_path)

    def predict(self, input_data):
        if self.model is None:
            # Ensure the model directory exists before attempting to load
            model_dir = os.path.dirname(self.model_path)
            if not os.path.exists(model_dir):
                raise FileNotFoundError(f"Model directory not found: {model_dir}. Please train the model first.")
            self.model = joblib.load(self.model_path)
            self.features = ['income', 'age'] # Re-initialize features for prediction if model is loaded later

        # Create a DataFrame from the input data, ensuring feature order
        df = pd.DataFrame([input_data.dict()])[self.features]
        
        prediction = self.model.predict(df)
        return prediction[0]

def predict_expense(input_data):
    predictor = ExpensePredictor()
    return predictor.predict(input_data)
