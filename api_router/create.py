from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database_ops.create_db import AddFirebase
from logger import logging

router = APIRouter(
    prefix='/create',
    tags=['create']
)

add_firebase_object = AddFirebase()

class UserRequest(BaseModel):
    username: str
    email: str
    phone: str
    password: str

class ExpenseRequest(BaseModel):
    user_id: str
    title: str
    category: str
    amount: float
    date: str

class BudgetRequest(BaseModel):
    user_id: str
    category: str
    amount: float
    period_in_days: int

class IncomeRequest(BaseModel):
    user_id: str
    source: str
    amount: float
    frequency: str
    date_received: str

class GoalRequest(BaseModel):
    user_id: str
    title: str
    target_amount: float
    deadline: str

class RecurringPaymentRequest(BaseModel):
    user_id: str
    service_name: str
    amount: float
    payment_date: str
    frequency: str
    auto_deduct: bool

class NotificationRequest(BaseModel):
    user_id: str
    message: str
    type: str


@router.post('/user')
async def create_user(payload: UserRequest):
    try:
        message = add_firebase_object.create_user(
            username=payload.username,
            email=payload.email,
            phone=payload.phone,
            password=payload.password
        )
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while adding new user: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post('/expense')
async def add_expense(payload: ExpenseRequest):
    try:
        message = add_firebase_object.add_expense(
            user_id=payload.user_id,
            title=payload.title,
            category=payload.category,
            amount=payload.amount,
            date=payload.date
        )
        logging.info(message)
        return message
    except Exception as e:
        logging.info(f"Error occurred while adding new expense: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post('/budget')
async def add_budget(payload: BudgetRequest):
    try:
        message = add_firebase_object.add_budget(
            user_id=payload.user_id,
            category=payload.category,
            amount=payload.amount,
            period_in_days=payload.period_in_days
        )
        logging.info(message)
        return message
    except Exception as e:
        logging.info(f"Error occurred while adding new budget: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post('/income')
async def add_income(payload: IncomeRequest):
    try:
        message = add_firebase_object.add_income(
            user_id=payload.user_id,
            source=payload.source,
            amount=payload.amount,
            frequency=payload.frequency,
            date_received=payload.date_received
        )
        logging.info(message)
        return message
    except Exception as e:
        logging.info(f"Error occurred while adding new income: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post('/goal')
async def add_goals(payload: GoalRequest):
    try:
        message = add_firebase_object.add_goals(
            user_id=payload.user_id,
            title=payload.title,
            target_amount=payload.target_amount,
            deadline=payload.deadline
        )
        logging.info(message)
        return message
    except Exception as e:
        logging.info(f"Error occurred while adding new goal: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post('/recurring-payment')
async def add_recurring_payments(payload: RecurringPaymentRequest):
    try:
        message = add_firebase_object.add_recurring_payments(
            user_id=payload.user_id,
            service_name=payload.service_name,
            amount=payload.amount,
            payment_date=payload.payment_date,
            frequency=payload.frequency,
            auto_deduct=payload.auto_deduct
        )
        logging.info(message)
        return message
    except Exception as e:
        logging.info(f"Error occurred while adding new recurring payment: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post('/notification')
async def add_notifications(payload: NotificationRequest):
    try:
        message = add_firebase_object.add_notification(
            user_id=payload.user_id,
            message=payload.message,
            type=payload.type
        )
        logging.info(message)
        return message
    except Exception as e:
        logging.info(f"Error occurred while adding new notification: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
