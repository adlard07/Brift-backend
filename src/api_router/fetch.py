from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from logger import logging
from src.database_ops.fetch import FetchFirebase

router = APIRouter(
    prefix='/fetch',
    tags=['fetch']
)

fetch_firebase_object = FetchFirebase()

class UserIDRequest(BaseModel):
    user_id: str

def handle_fetch(fetch_function, user_id: str):
    """
    Generic function to handle fetch responses.
    Handles exceptions and logs messages.

    Args:
        fetch_function (Callable): The function to call to fetch data.
        user_id (str): The user's unique identifier.

    Returns:
        dict: Fetched data from Firebase.

    Raises:
        HTTPException: If any error occurs while fetching.
    """
    try:
        message = fetch_function(user_id)
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while fetching: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error")

@router.post('/user')
async def fetch_user(payload: UserIDRequest):
    '''
    Fetches complete user profile information from Firebase.

    Sample Output:
    {
        "created_at": "2025-05-04 16:52:51.591983",
        "device_id": "12394012964",
        "email": "adelarddcunha@gmail.com",
        "last_login": "2025-05-04 16:52:51.591983",
        "mfa_enabled": false,
        "name": "Adelard",
        "password": "...",
        "points": 10,
        "store_unlocked": false
    }

    Args:
        user_id (str): Unique identifier of the user

    Returns:
        dict: User profile information
    '''
    return handle_fetch(fetch_firebase_object.fetch_user, payload.user_id)

@router.post('/expenses')
async def fetch_expenses(payload: UserIDRequest):
    '''
    Fetches all recorded expenses for the given user from Firebase.

    Each expense includes details like category, amount, date, and payment method.

    Returns:
        dict: All expense entries
    '''
    return handle_fetch(lambda user_id: fetch_firebase_object.fetch_data(user_id, 'expenses'), payload.user_id)

@router.post('/budgets')
async def fetch_budgets(payload: UserIDRequest):
    '''
    Fetches all budget settings for the user from Firebase.

    Each budget includes category, monthly limit, and additional notes.

    Returns:
        dict: All budget entries
    '''
    return handle_fetch(lambda user_id: fetch_firebase_object.fetch_data(user_id, 'budgets'), payload.user_id)

@router.post('/income')
async def fetch_income(payload: UserIDRequest):
    '''
    Fetches all income sources for the user from Firebase.

    Each entry includes the income source, title, amount received, and date.

    Returns:
        dict: All income entries
    '''
    return handle_fetch(lambda user_id: fetch_firebase_object.fetch_data(user_id, 'incomes'), payload.user_id)

@router.post('/goals')
async def fetch_goals(payload: UserIDRequest):
    '''
    Fetches all financial goals set by the user from Firebase.

    Each goal includes a title, target amount, due date, and completion status.

    Returns:
        dict: All goal entries
    '''
    return handle_fetch(lambda user_id: fetch_firebase_object.fetch_data(user_id, 'goals'), payload.user_id)

@router.post('/bills')
async def fetch_bills(payload: UserIDRequest):
    '''
    Fetches all upcoming or recurring bills for the user from Firebase.

    Each bill includes the title, due date, amount, and recurring status.

    Returns:
        dict: All bill entries
    '''
    return handle_fetch(lambda user_id: fetch_firebase_object.fetch_data(user_id, 'bills'), payload.user_id)

@router.post('/reminders')
async def fetch_reminders(payload: UserIDRequest):
    '''
    Fetches all active reminders for the user from Firebase.

    Each reminder includes a title, description, reminder time, and linked item.

    Returns:
        dict: All reminder entries
    '''
    return handle_fetch(lambda user_id: fetch_firebase_object.fetch_data(user_id, 'reminders'), payload.user_id)

@router.post('/notifications')
async def fetch_notifications(payload: UserIDRequest):
    '''
    Fetches all unread or active notifications for the user from Firebase.

    Each notification includes a message, type, and read status.

    Returns:
        dict: All notification entries
    '''
    return handle_fetch(lambda user_id: fetch_firebase_object.fetch_data(user_id, 'notifications'), payload.user_id)

@router.post('/debt')
async def fetch_debt(payload: UserIDRequest):
    '''
    Fetches all outstanding debts for the user from Firebase.

    Each debt includes total and remaining amount, due date, interest rate, and title.

    Returns:
        dict: All debt entries
    '''
    return handle_fetch(lambda user_id: fetch_firebase_object.fetch_data(user_id, 'debts'), payload.user_id)

@router.post('/investment')
async def fetch_investment(payload: UserIDRequest):
    '''
    Fetches all investments made by the user from Firebase.

    Each investment includes title, amount invested, current value, and date.

    Returns:
        dict: All investment entries
    '''
    return handle_fetch(lambda user_id: fetch_firebase_object.fetch_data(user_id, 'investments'), payload.user_id)
