from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class TransactionCreate(BaseModel):
    date: datetime
    category: str
    amount: float
    description: Optional[str] = None

class Transaction(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    user_id: str
    date: datetime
    category: str
    amount: float
    description: Optional[str] = None

class Expense(Transaction):
    pass

class Income(Transaction):
    pass

class Budget(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    user_id: str
    category: str
    amount: float
    start_date: datetime
    end_date: datetime
