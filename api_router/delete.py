from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database_ops.delete_db import DeleteFirebase
from logger import logging

router = APIRouter(
    prefix='/delete',
    tags=['delete']
)

delete_firebase_db = DeleteFirebase()

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

class RecurringPaymentRequest(BaseModel):
    user_id: str
    payment_id: str

class NotificationRequest(BaseModel):
    user_id: str
    notification_id: str


@router.delete('/user')
async def delete_user(payload: UserRequest):
    try:
        message = delete_firebase_db.delete_user(payload.user_id)
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while deleting user: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.delete('/expense')
async def delete_expense(payload: ExpenseRequest):
    try:
        message = delete_firebase_db.delete_expense(payload.user_id, payload.expense_id)
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while deleting expense: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.delete('/budget')
async def delete_budget(payload: BudgetRequest):
    try:
        message = delete_firebase_db.delete_budget(payload.user_id, payload.budget_id)
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while deleting budget: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.delete('/income')
async def delete_income(payload: IncomeRequest):
    try:
        message = delete_firebase_db.delete_income(payload.user_id, payload.income_id)
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while deleting income: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.delete('/goal')
async def delete_goal(payload: GoalRequest):
    try:
        message = delete_firebase_db.delete_goal(payload.user_id, payload.goal_id)
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while deleting goal: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.delete('/recurring-payment')
async def delete_recurring_payment(payload: RecurringPaymentRequest):
    try:
        message = delete_firebase_db.delete_recurring_payment(payload.user_id, payload.payment_id)
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while deleting recurring payment: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.delete('/notification')
async def delete_notification(payload: NotificationRequest):
    try:
        message = delete_firebase_db.delete_notification(payload.user_id, payload.notification_id)
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while deleting notification: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
