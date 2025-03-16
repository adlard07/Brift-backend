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

class RecurringPaymentRequest(BaseModel):
    user_id: str
    payment_id: str
    service_name: str = None
    amount: float = None
    frequency: str = None
    auto_deduct: bool = None

class NotificationRequest(BaseModel):
    user_id: str
    notification_id: str
    message: str = None
    read: bool = None
    

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

@router.patch('/expense')
async def update_expense(payload: ExpenseRequest):
    try:
        message = update_firebase_db.update_expense(
            user_id=payload.user_id,
            expense_id=payload.expense_id,
            title=payload.title,
            category=payload.category,
            amount=payload.amount,
            date=payload.date
        )
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while updating expense: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.patch('/budget')
async def update_budget(payload: BudgetRequest):
    try:
        message = update_firebase_db.update_budget(
            user_id=payload.user_id,
            budget_id=payload.budget_id,
            category=payload.category,
            amount=payload.amount,
            period_in_days=payload.period_in_days
        )
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while updating budget: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.patch('/income')
async def update_income(payload: IncomeRequest):
    try:
        message = update_firebase_db.update_income(
            user_id=payload.user_id,
            income_id=payload.income_id,
            source=payload.source,
            amount=payload.amount,
            frequency=payload.frequency
        )
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while updating income: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.patch('/goal')
async def update_goal(payload: GoalRequest):
    try:
        message = update_firebase_db.update_goal(
            user_id=payload.user_id,
            goal_id=payload.goal_id,
            title=payload.title,
            target_amount=payload.target_amount,
            saved_amount=payload.saved_amount,
            status=payload.status
        )
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while updating goal: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.patch('/recurring-payment')
async def update_recurring_payment(payload: RecurringPaymentRequest):
    try:
        message = update_firebase_db.update_recurring_payment(
            user_id=payload.user_id,
            payment_id=payload.payment_id,
            service_name=payload.service_name,
            amount=payload.amount,
            frequency=payload.frequency,
            auto_deduct=payload.auto_deduct
        )
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while updating recurring payment: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.patch('/notification')
async def update_notification(payload: NotificationRequest):
    try:
        message = update_firebase_db.update_notification(
            user_id=payload.user_id,
            notification_id=payload.notification_id,
            message=payload.message,
            read=payload.read
        )
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while updating notification: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
