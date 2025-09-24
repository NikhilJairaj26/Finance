from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..models.finance import Transaction, TransactionCreate, Expense, Income, Budget
from ..models.user import User
from ..utils.auth import get_current_user
from ..database import db
from bson import ObjectId

router = APIRouter()

@router.post("/transactions", response_model=Transaction)
def create_transaction(transaction_data: TransactionCreate, current_user: User = Depends(get_current_user)):
    transaction = Transaction(
        user_id=current_user.email,
        date=transaction_data.date,
        category=transaction_data.category,
        amount=transaction_data.amount,
        description=transaction_data.description
    )
    transaction_dict = transaction.dict(by_alias=True)
    if transaction_dict.get("_id") is None:
        transaction_dict.pop("_id", None) # Remove _id if it's None

    result = db.transactions.insert_one(transaction_dict)
    created_transaction = db.transactions.find_one({"_id": result.inserted_id})

    # Explicitly convert ObjectId to string for the response
    if created_transaction and "_id" in created_transaction:
        created_transaction["_id"] = str(created_transaction["_id"])
    
    return created_transaction

@router.get("/transactions", response_model=List[Transaction])
def get_transactions(current_user: User = Depends(get_current_user)):
    transactions = list(db.transactions.find({"user_id": current_user.email}))
    
    # Explicitly convert ObjectId to string for each transaction in the list
    for transaction in transactions:
        if "_id" in transaction:
            transaction["_id"] = str(transaction["_id"])
            
    return transactions

# Add more endpoints for Expense, Income, Budget as needed
