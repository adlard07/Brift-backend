from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database_ops.fetch_db import FetchFirebase
from logger import logging

router = APIRouter(
    prefix='/fetch',
    tags=['fetch']
)

fetch_firebase_object = FetchFirebase()

class UserIDRequest(BaseModel):
    user_id: str

@router.post('/user')
async def fetch_user(payload: UserIDRequest):
    try:
        message = fetch_firebase_object.fetch_user(
            user_id=payload.user_id
        )
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while fetching user: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post('/expenses')
async def fetch_expenses(payload: UserIDRequest):
    try:
        message = fetch_firebase_object.fetch_expenses(
            user_id=payload.user_id
        )
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while fetching expenses: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post('/budgets')
async def fetch_budgets(payload: UserIDRequest):
    try:
        message = fetch_firebase_object.fetch_budgets(
            user_id=payload.user_id
        )
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while fetching budgets: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post('/income')
async def fetch_income(payload: UserIDRequest):
    try:
        message = fetch_firebase_object.fetch_income(
            user_id=payload.user_id
        )
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while fetching incomes: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post('/goals')
async def fetch_goals(payload: UserIDRequest):
    try:
        message = fetch_firebase_object.fetch_goals(
            user_id=payload.user_id
        )
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while fetching goals: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post('/recurring-payments')
async def fetch_recurring_payments(payload: UserIDRequest):
    try:
        message = fetch_firebase_object.fetch_recurring_payments(
            user_id=payload.user_id
        )
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while fetching recurring payments: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post('/notifications')
async def fetch_notifications(payload: UserIDRequest):
    try:
        message = fetch_firebase_object.fetch_notifications(
            user_id=payload.user_id
        )
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while fetching notifications: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
