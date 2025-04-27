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
        message = fetch_firebase_object.fetch_user(user_id=payload.user_id)
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while fetching user: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post('/expenses')
async def fetch_expenses(payload: UserIDRequest):
    try:
        message = fetch_firebase_object.fetch_expenses(user_id=payload.user_id)
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while fetching expenses: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post('/budgets')
async def fetch_budgets(payload: UserIDRequest):
    try:
        message = fetch_firebase_object.fetch_budgets(user_id=payload.user_id)
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while fetching budgets: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post('/income')
async def fetch_income(payload: UserIDRequest):
    try:
        message = fetch_firebase_object.fetch_income(user_id=payload.user_id)
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while fetching incomes: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post('/goals')
async def fetch_goals(payload: UserIDRequest):
    try:
        message = fetch_firebase_object.fetch_goals(user_id=payload.user_id)
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while fetching goals: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post('/bills')
async def fetch_bills(payload: UserIDRequest):
    try:
        message = fetch_firebase_object.fetch_bills(user_id=payload.user_id)
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while fetching bills: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post('/reminders')
async def fetch_reminders(payload: UserIDRequest):
    try:
        message = fetch_firebase_object.fetch_reminders(user_id=payload.user_id)
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while fetching reminders: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post('/notifications')
async def fetch_notifications(payload: UserIDRequest):
    try:
        message = fetch_firebase_object.fetch_notifications(user_id=payload.user_id)
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while fetching notifications: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post('/debt')
async def fetch_debt(payload: UserIDRequest):
    try:
        message = fetch_firebase_object.fetch_debt(user_id=payload.user_id)
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while fetching debt: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post('/investment')
async def fetch_investment(payload: UserIDRequest):
    try:
        message = fetch_firebase_object.fetch_investment(user_id=payload.user_id)
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while fetching investment: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
