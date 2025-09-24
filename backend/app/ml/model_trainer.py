from .expense_predictor import ExpensePredictor

def train_models():
    print("Training Expense Predictor model...")
    expense_predictor = ExpensePredictor()
    expense_predictor.train()
    print("Expense Predictor model trained successfully.")

    # Add training for other models here

if __name__ == "__main__":
    train_models()
