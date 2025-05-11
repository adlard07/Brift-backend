from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from logger import logging
from src.database_ops.fetch_db import FetchFirebase

router = APIRouter(
    prefix='/fetch',
    tags=['fetch']
)

fetch_firebase_object = FetchFirebase()

class UserIDRequest(BaseModel):
    user_id: str

def handle_fetch(fetch_function, user_id: str):
    """Generic function to handle fetch responses."""
    try:
        message = fetch_function(user_id)
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while fetching: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error")

@router.post('/user')
async def fetch_user(payload: UserIDRequest):
    return handle_fetch(fetch_firebase_object.fetch_user, payload.user_id)

@router.post('/expenses')
async def fetch_expenses(payload: UserIDRequest):
    return handle_fetch(lambda user_id: fetch_firebase_object.fetch_data(user_id, 'expenses'), payload.user_id)

@router.post('/budgets')
async def fetch_budgets(payload: UserIDRequest):
    return handle_fetch(lambda user_id: fetch_firebase_object.fetch_data(user_id, 'budgets'), payload.user_id)

@router.post('/income')
async def fetch_income(payload: UserIDRequest):
    return handle_fetch(lambda user_id: fetch_firebase_object.fetch_data(user_id, 'income'), payload.user_id)

@router.post('/goals')
async def fetch_goals(payload: UserIDRequest):
    return handle_fetch(lambda user_id: fetch_firebase_object.fetch_data(user_id, 'goals'), payload.user_id)

@router.post('/bills')
async def fetch_bills(payload: UserIDRequest):
    return handle_fetch(lambda user_id: fetch_firebase_object.fetch_data(user_id, 'bills'), payload.user_id)

@router.post('/reminders')
async def fetch_reminders(payload: UserIDRequest):
    return handle_fetch(lambda user_id: fetch_firebase_object.fetch_data(user_id, 'reminders'), payload.user_id)

@router.post('/notifications')
async def fetch_notifications(payload: UserIDRequest):
    return handle_fetch(lambda user_id: fetch_firebase_object.fetch_data(user_id, 'notifications'), payload.user_id)

@router.post('/debt')
async def fetch_debt(payload: UserIDRequest):
    return handle_fetch(lambda user_id: fetch_firebase_object.fetch_data(user_id, 'debt'), payload.user_id)

@router.post('/investment')
async def fetch_investment(payload: UserIDRequest):
    return handle_fetch(lambda user_id: fetch_firebase_object.fetch_data(user_id, 'investments'), payload.user_id)
