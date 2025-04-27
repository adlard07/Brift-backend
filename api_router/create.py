from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database_ops.create_db import AddFirebase
from logger import logging
from datetime import datetime
from typing import Optional


router = APIRouter(
    prefix='/create',
    tags=['create']
)

add_firebase_object = AddFirebase()

# ------------------------- Models -------------------------

class UserRequest(BaseModel):
    name: str
    email: str
    phone: str
    device_id: str
    created_at: str = str(datetime.now())
    points: int
    store_unlocked: bool
    mfa_enabled: bool
    last_login: str = str(datetime.now())

    currency: str
    region: str
    backup_enabled: bool


class ExpenseRequest(BaseModel):
    user_id: str
    amount: float
    category: str
    date: str = str(datetime.now())
    notes: Optional[str] = ""
    payment_method: Optional[str] = "cash"
    is_recurring: Optional[bool] = False

class BudgetRequest(BaseModel):
    user_id: str
    category: str
    note: Optional[str] = ""
    amount_limit: float
    interval: str

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
    is_paid: bool = False
    recurring: bool = False

class ReminderRequest(BaseModel):
    user_id: str
    title: str
    description: str
    remind_at: str
    linked_to: Optional[str] = None

class NotificationRequest(BaseModel):
    user_id: str
    type: str
    message: str
    is_read: bool = False
    is_valid: bool = True

class DebtRequest(BaseModel):
    user_id: str
    type: str
    total_amount: float
    remaining_amount: float
    interest_rate: float
    due_date: str

class InvestmentRequest(BaseModel):
    user_id: str
    type: str
    amount_invested: float
    current_value: float
    date_invested: str
    notes: Optional[str] = ""


# ------------------------- Routes -------------------------


@router.post('/user') 
async def create_user(payload: UserRequest):
    try:
        profile = {
            "name": payload.name,
            "email": payload.email,
            "phone": payload.phone,
            "device_id": payload.device_id,
            "created_at": payload.last_login,
            "points": payload.points,
            "store_unlocked": payload.store_unlocked,
            "mfa_enabled": payload.mfa_enabled,
            "last_login": payload.last_login,
        }

        settings = {
            "currency": payload.currency,
            "region": payload.region,
            "backup_enabled": payload.backup_enabled,
        }

        message = add_firebase_object.create_user(profile, settings)

        if message.get("status_code") != 201:
            raise HTTPException(status_code=message.get("status_code", 500), detail=message.get("error", "Unknown error"))

        logging.info(message)
        return message

    except Exception as e:
        logging.error(f"Error occurred while adding new user: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error {e}")



@router.post('/expense')
async def add_expense(payload: ExpenseRequest):
    try:
        expense = {
            "user_id": payload.user_id,
            "amount": payload.amount,
            "category": payload.category,
            "date": str(datetime.now()),
            "notes": payload.notes,
            "payment_method": payload.payment_method,
            "is_recurring": payload.is_recurring,
            }

        message = add_firebase_object.add_expense(expense)

        if message.get("status_code") != 201:
            raise HTTPException(status_code=message.get("status_code", 500), detail=message.get("error", "Unknown error"))

        logging.info(message)
        return message
    except Exception as e:
        logging.info(f"Error occurred while adding new expense: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error {e}")



@router.post('/budget')
async def add_budget(payload: BudgetRequest):
    try:
        budget = {
            "user_id": payload.user_id,
            "category": payload.category,
            "note": payload.note,
            "amount_limit": payload.amount_limit,
            "interval": payload.interval,
            }

        message = add_firebase_object.add_budget(budget)

        if message.get("status_code") != 201:
            raise HTTPException(status_code=message.get("status_code", 500), detail=message.get("error", "Unknown error"))

        logging.info(message)
        return message
    except Exception as e:
        logging.info(f"Error occurred while adding new budget: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")



@router.post('/income')
async def add_income(payload: IncomeRequest):
    try:
        income = {    
            "user_id": payload.user_id,
            "source": payload.source,
            "title": payload.title,
            "amount": payload.amount,
            "date_received": payload.date_received,
            "notes": payload.notes,
            }

        message = add_firebase_object.add_income(income)
        if message.get("status_code") != 201:
            raise HTTPException(status_code=message.get("status_code", 500), detail=message.get("error", "Unknown error"))

        logging.info(message)
        return message
    except Exception as e:
        logging.info(f"Error occurred while adding new income: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post('/goal')
async def add_goals(payload: GoalRequest):
    try:
        goal = {
            "user_id": payload.user_id,
            "title": payload.title,
            "target_amount": payload.target_amount,
            "due_date": payload.due_date,
            "status": payload.status,
            }

        message = add_firebase_object.add_goals(goal)
        if message.get("status_code") != 201:
            raise HTTPException(status_code=message.get("status_code", 500), detail=message.get("error", "Unknown error"))

        logging.info(message)
        return message
    except Exception as e:
        logging.info(f"Error occurred while adding new goal: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post('/bill')
async def add_bill(payload: BillRequest):
    try:
        bill = {
            "user_id": payload.user_id,
            "title": payload.title,
            "amount": payload.amount,
            "due_date": payload.due_date,
            "is_paid": payload.is_paid,
            "recurring": payload.recurring
        }

        message = add_firebase_object.add_bill(bill)
        if message.get("status_code") != 201:
            raise HTTPException(status_code=message.get("status_code", 500), detail=message.get("error", "Unknown error"))

        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while adding new bill: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post('/reminder')
async def add_reminder(payload: ReminderRequest):
    try:
        reminder = {
            "user_id": payload.user_id,
            "title": payload.title,
            "description": payload.description,
            "remind_at": payload.remind_at,
            "linked_to": payload.linked_to
        }

        message = add_firebase_object.add_reminder(reminder)
        if message.get("status_code") != 201:
            raise HTTPException(status_code=message.get("status_code", 500), detail=message.get("error", "Unknown error"))

        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while adding new reminder: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")



@router.post('/notification')
async def add_notifications(payload: NotificationRequest):
    try:
        notification = {
            "user_id": payload.user_id,
            "type": payload.type,
            "message": payload.message,
            "is_read": payload.is_read,
            "is_valid": payload.is_valid
        }

        message = add_firebase_object.add_notification(notification)
        if message.get("status_code") != 201:
            raise HTTPException(status_code=message.get("status_code", 500), detail=message.get("error", "Unknown error"))

        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while adding new notification: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")



@router.post('/debt')
async def add_debt(payload: DebtRequest):
    try:
        debt = {
            "user_id": payload.user_id,
            "type": payload.type,
            "total_amount": payload.total_amount,
            "remaining_amount": payload.remaining_amount,
            "interest_rate": payload.interest_rate,
            "due_date": payload.due_date,
        }

        message = add_firebase_object.add_debt(debt)
        if message.get("status_code") != 201:
            raise HTTPException(status_code=message.get("status_code", 500), detail=message.get("error", "Unknown error"))

        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while adding new debt: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")



@router.post('/investment')
async def add_investment(payload: InvestmentRequest):
    try:
        investment = {
            "user_id": payload.user_id,
            "type": payload.type,
            "amount_invested": payload.amount_invested,
            "current_value": payload.current_value,
            "date_invested": payload.date_invested,
            "notes": payload.notes
        }

        message = add_firebase_object.add_investment(investment)
        if message.get("status_code") != 201:
            raise HTTPException(status_code=message.get("status_code", 500), detail=message.get("error", "Unknown error"))

        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while adding new investment: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

