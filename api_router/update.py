from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database_ops.update_db import UpdateFirebase
from logger import logging

router = APIRouter(
    prefix='/update',
    tags=['update']
)

update_firebase_db = UpdateFirebase()

class UserRequest(BaseModel):
    user_id: str
    username: str = None
    email: str = None
    password: str = None

class ExpenseRequest(BaseModel):
    user_id: str
    expense_id: str
    title: str = None
    category: str = None
    amount: float = None
    date: str = None

class BudgetRequest(BaseModel):
    user_id: str
    budget_id: str
    category: str = None
    amount: float = None
    period_in_days: int = None

class IncomeRequest(BaseModel):
    user_id: str
    income_id: str
    source: str = None
    amount: float = None
    frequency: str = None

class GoalRequest(BaseModel):
    user_id: str
    goal_id: str
    title: str = None
    target_amount: float = None
    saved_amount: float = None
    status: str = None

class NotificationRequest(BaseModel):
    user_id: str
    notification_id: str
    message: str = None
    read: bool = None

class BillRequest(BaseModel):
    user_id: str
    bill_id: str
    title: str = None
    amount: float = None
    due_date: str = None
    is_paid: bool = None
    recurring: bool = None

class ReminderRequest(BaseModel):
    user_id: str
    reminder_id: str
    title: str = None
    description: str = None
    remind_at: str = None
    linked_to: str = None

class DebtRequest(BaseModel):
    user_id: str
    debt_id: str
    type: str = None
    total_amount: float = None
    remaining_amount: float = None
    interest_rate: float = None
    due_date: str = None

class InvestmentRequest(BaseModel):
    user_id: str
    investment_id: str
    type: str = None
    amount_invested: float = None
    current_value: float = None
    date_invested: str = None
    notes: str = None

# Existing Routes...

@router.patch('/user')
async def update_user(payload: UserRequest):
    try:
        message = update_firebase_db.update_user(
            user_id=payload.user_id,
            username=payload.username,
            email=payload.email,
            password=payload.password
        )
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while updating user: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

# ... Other existing routes (expense, budget, income, goal, notification) ...

# Newly Added Routes

@router.patch('/bill')
async def update_bill(payload: BillRequest):
    try:
        message = update_firebase_db.update_bill(
            user_id=payload.user_id,
            bill_id=payload.bill_id,
            title=payload.title,
            amount=payload.amount,
            due_date=payload.due_date,
            is_paid=payload.is_paid,
            recurring=payload.recurring
        )
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while updating bill: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.patch('/reminder')
async def update_reminder(payload: ReminderRequest):
    try:
        message = update_firebase_db.update_reminder(
            user_id=payload.user_id,
            reminder_id=payload.reminder_id,
            title=payload.title,
            description=payload.description,
            remind_at=payload.remind_at,
            linked_to=payload.linked_to
        )
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while updating reminder: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.patch('/debt')
async def update_debt(payload: DebtRequest):
    try:
        message = update_firebase_db.update_debt(
            user_id=payload.user_id,
            debt_id=payload.debt_id,
            type=payload.type,
            total_amount=payload.total_amount,
            remaining_amount=payload.remaining_amount,
            interest_rate=payload.interest_rate,
            due_date=payload.due_date
        )
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while updating debt: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.patch('/investment')
async def update_investment(payload: InvestmentRequest):
    try:
        message = update_firebase_db.update_investment(
            user_id=payload.user_id,
            investment_id=payload.investment_id,
            type=payload.type,
            amount_invested=payload.amount_invested,
            current_value=payload.current_value,
            date_invested=payload.date_invested,
            notes=payload.notes
        )
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while updating investment: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
