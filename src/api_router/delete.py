from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from src.database_ops.delete_db import DeleteFirebase
from logger import logging

router = APIRouter(
    prefix='/delete',
    tags=['delete']
)

delete_firebase_db = DeleteFirebase()

# ------------------------- Models -------------------------

class UserRequest(BaseModel):
    user_id: str

class ExpenseRequest(BaseModel):
    user_id: str
    expense_id: str

class BudgetRequest(BaseModel):
    user_id: str
    budget_id: str

class IncomeRequest(BaseModel):
    user_id: str
    income_id: str

class GoalRequest(BaseModel):
    user_id: str
    goal_id: str

class NotificationRequest(BaseModel):
    user_id: str
    notification_id: str

class BillRequest(BaseModel):
    user_id: str
    bill_id: str

class ReminderRequest(BaseModel):
    user_id: str
    reminder_id: str

class DebtRequest(BaseModel):
    user_id: str
    debt_id: str

class InvestmentRequest(BaseModel):
    user_id: str
    investment_id: str

# ------------------------- Generic Handler -------------------------

def handle_delete(delete_function, payload_data: dict):
    try:
        message = delete_function(**payload_data)
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while deleting: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

# ------------------------- Delete Routes -------------------------

@router.delete('/user')
async def delete_user(payload: UserRequest):
    return handle_delete(delete_firebase_db.delete_user, {"user_id": payload.user_id})

@router.delete('/expense')
async def delete_expense(payload: ExpenseRequest):
    return handle_delete(delete_firebase_db.delete_expense, payload.dict())

@router.delete('/budget')
async def delete_budget(payload: BudgetRequest):
    return handle_delete(delete_firebase_db.delete_budget, payload.dict())

@router.delete('/income')
async def delete_income(payload: IncomeRequest):
    return handle_delete(delete_firebase_db.delete_income, payload.dict())

@router.delete('/goal')
async def delete_goal(payload: GoalRequest):
    return handle_delete(delete_firebase_db.delete_goal, payload.dict())

@router.delete('/notification')
async def delete_notification(payload: NotificationRequest):
    return handle_delete(delete_firebase_db.delete_notification, payload.dict())

@router.delete('/bill')
async def delete_bill(payload: BillRequest):
    return handle_delete(delete_firebase_db.delete_bill, payload.dict())

@router.delete('/reminder')
async def delete_reminder(payload: ReminderRequest):
    return handle_delete(delete_firebase_db.delete_reminder, payload.dict())

@router.delete('/debt')
async def delete_debt(payload: DebtRequest):
    return handle_delete(delete_firebase_db.delete_debt, payload.dict())

@router.delete('/investment')
async def delete_investment(payload: InvestmentRequest):
    return handle_delete(delete_firebase_db.delete_investment, payload.dict())
