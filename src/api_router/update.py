from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from src.database_ops.update_db import UpdateFirebase
from logger import logging

router = APIRouter(
    prefix='/update',
    tags=['update']
)

update_firebase_db = UpdateFirebase()

class UserRequest(BaseModel):
    user_id: str
    username: str = None
    password: str = None

class ExpenseRequest(BaseModel):
    user_id: str
    expense_id: str
    title: str = None
    category: str = None
    amount: float = None
    date: str = None
    payment_method: str = None

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
 

# ---------------------- Generic Handler for Update Routes ------------------------------------


def handle_update(update_function, payload_data: dict):
    """Generic function to handle update responses."""
    try:
        message = update_function(**payload_data)
        logging.info(message)
        return message
    except Exception as e:
        logging.error(f"Error occurred while updating data: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


# -------------------- Update Routes --------------------------------------


@router.patch('/user')
async def update_user(payload: UserRequest):
    return handle_update(update_firebase_db.update_user, payload.dict(exclude_unset=True))

@router.patch('/expense')
async def update_expense(payload: ExpenseRequest):
    return handle_update(update_firebase_db.update_expense, payload.dict(exclude_unset=True))

@router.patch('/budget')
async def update_budget(payload: BudgetRequest):
    return handle_update(update_firebase_db.update_budget, payload.dict(exclude_unset=True))

@router.patch('/income')
async def update_income(payload: IncomeRequest):
    return handle_update(update_firebase_db.update_income, payload.dict(exclude_unset=True))

@router.patch('/goal')
async def update_goal(payload: GoalRequest):
    return handle_update(update_firebase_db.update_goal, payload.dict(exclude_unset=True))

@router.patch('/notification')
async def update_notification(payload: NotificationRequest):
    return handle_update(update_firebase_db.update_notification, payload.dict(exclude_unset=True))

@router.patch('/bill')
async def update_bill(payload: BillRequest):
    return handle_update(update_firebase_db.update_bill, payload.dict(exclude_unset=True))

@router.patch('/reminder')
async def update_reminder(payload: ReminderRequest):
    return handle_update(update_firebase_db.update_reminder, payload.dict(exclude_unset=True))

@router.patch('/debt')
async def update_debt(payload: DebtRequest):
    return handle_update(update_firebase_db.update_debt, payload.dict(exclude_unset=True))

@router.patch('/investment')
async def update_investment(payload: InvestmentRequest):
    return handle_update(update_firebase_db.update_investment, payload.dict(exclude_unset=True))
