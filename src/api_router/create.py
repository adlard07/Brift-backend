from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from src.database_ops.create_db import AddFirebase
from logger import logging


router = APIRouter(
    prefix='/create',
    tags=['create']
)

add_firebase_object = AddFirebase()

# ------------------------- Models -------------------------

class UserRequest(BaseModel):
    name: str
    email: str
    password: str
    phone: Optional[str] = None
    device_id: str
    points: int
    store_unlocked: bool
    mfa_enabled: bool
    currency: str
    region: str
    backup_enabled: bool
    created_at: Optional[str] = str(datetime.now())
    last_login: Optional[str] = str(datetime.now())

class ExpenseRequest(BaseModel):
    user_id: str
    amount: float
    category: str
    notes: Optional[str] = ""
    payment_method: Optional[str] = "cash"
    is_recurring: Optional[bool] = False
    date: Optional[str] = str(datetime.now())

class BudgetRequest(BaseModel):
    user_id: str
    category: str
    amount_limit: float
    interval: str
    note: Optional[str] = ""

class IncomeRequest(BaseModel):
    user_id: str
    source: str
    title: str
    amount: float
    date_received: str
    notes: Optional[str] = ""

class GoalRequest(BaseModel):
    user_id: str
    title: str
    target_amount: float
    due_date: str
    status: Optional[bool] = False

class BillRequest(BaseModel):
    user_id: str
    title: str
    amount: float
    due_date: str
    is_paid: Optional[bool] = False
    recurring: Optional[bool] = False

class ReminderRequest(BaseModel):
    user_id: str
    title: str
    description: str
    remind_at: str
    linked_to: Optional[str] = None

class NotificationRequest(BaseModel):
    user_id: str
    notification_type: str
    message: str
    is_read: Optional[bool] = False
    is_valid: Optional[bool] = True

class DebtRequest(BaseModel):
    user_id: str
    title: str
    total_amount: float
    remaining_amount: float
    interest_rate: float
    due_date: str

class InvestmentRequest(BaseModel):
    user_id: str
    title: str
    amount_invested: float
    current_value: float
    date_invested: str
    notes: Optional[str] = ""

# ------------------------- Routes -------------------------

def handle_firebase_response(message: dict):
    if message.get("status_code") != 201:
        raise HTTPException(status_code=message.get("status_code", 500), detail=message.get("error", "Unknown error"))
    logging.info(message)
    return message
    

@router.post('/users') 
async def create_user(payload: UserRequest):
    try:
        profile = payload.dict(include={
            'name', 'email', 'password', 'phone', 'device_id', 'created_at', 'points',
            'store_unlocked', 'mfa_enabled', 'last_login'
        })
        settings = payload.dict(include={'currency', 'region', 'backup_enabled'})

        message = add_firebase_object.create_user(profile, settings)
        return handle_firebase_response(message)
    except Exception as e:
        logging.error(f"Error occurred while adding new user: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error {e}")


@router.post('/expenses')
async def add_expense(payload: ExpenseRequest):
    try:
        payload.dict()['date'] = datetime.now()
        message = add_firebase_object.add_expense(payload.dict())
        return handle_firebase_response(message)
    except Exception as e:
        logging.error(f"Error occurred while adding new expense: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error {e}")

@router.post('/budgets')
async def add_budget(payload: BudgetRequest):
    try:
        message = add_firebase_object.add_budget(payload.dict())
        return handle_firebase_response(message)
    except Exception as e:
        logging.error(f"Error occurred while adding new budget: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error {e}")

@router.post('/incomes')
async def add_income(payload: IncomeRequest):
    try:
        message = add_firebase_object.add_income(payload.dict())
        return handle_firebase_response(message)
    except Exception as e:
        logging.error(f"Error occurred while adding new income: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error {e}")

@router.post('/goals')
async def add_goal(payload: GoalRequest):
    try:
        message = add_firebase_object.add_goal(payload.dict())
        return handle_firebase_response(message)
    except Exception as e:
        logging.error(f"Error occurred while adding new goal: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error {e}")

@router.post('/bills')
async def add_bill(payload: BillRequest):
    try:
        message = add_firebase_object.add_bill(payload.dict())
        return handle_firebase_response(message)
    except Exception as e:
        logging.error(f"Error occurred while adding new bill: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error {e}")

@router.post('/reminders')
async def add_reminder(payload: ReminderRequest):
    try:
        message = add_firebase_object.add_reminder(payload.dict())
        return handle_firebase_response(message)
    except Exception as e:
        logging.error(f"Error occurred while adding new reminder: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error {e}")

@router.post('/notifications')
async def add_notification(payload: NotificationRequest):
    try:
        message = add_firebase_object.add_notification(payload.dict())
        return handle_firebase_response(message)
    except Exception as e:
        logging.error(f"Error occurred while adding new notification: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error {e}")

@router.post('/debts')
async def add_debt(payload: DebtRequest):
    try:
        message = add_firebase_object.add_debt(payload.dict())
        return handle_firebase_response(message)
    except Exception as e:
        logging.error(f"Error occurred while adding new debt: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error {e}")

@router.post('/investments')
async def add_investment(payload: InvestmentRequest):
    try:
        message = add_firebase_object.add_investment(payload.dict())
        return handle_firebase_response(message)
    except Exception as e:
        logging.error(f"Error occurred while adding new investment: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error {e}")
