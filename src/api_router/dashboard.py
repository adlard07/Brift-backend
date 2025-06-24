from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from logger import logging

from src.models.dashboard import Dashboard
from src.models.QnA import QnA

router = APIRouter(
    prefix='/dashboard',
    tags=['dashboard'])

# ------------------------- Models -------------------------

class UserRequest(BaseModel):
    user_id: str

class QnARequest(BaseModel):
    user_query: str
    user_id: str

# ------------------------- Routes -------------------------

@router.post('/total_spending')
async def dashboard(payload: UserRequest):
    try:
        dashboard_obj = Dashboard(user_id=payload.user_id)
        result = dashboard_obj.total_spending()
        return result
    except Exception as e:
        logging.error(f"Error occurred as: {e}")
        raise HTTPException(status_code=500, detail=f'Could not fetch dashboard data due to: {e}')


@router.post('/budgets')
async def budgets(payload: UserRequest):
    try:
        budget_obj = Dashboard(user_id=payload.user_id)
        result = budget_obj.get_budgets()
        return result
    except Exception as e:
        logging.error(f"Error occurred as: {e}")
        raise HTTPException(status_code=500, detail=f'Could not fetch budgets data due to: {e}')


@router.post('/transactions')
async def transactions(payload: UserRequest):
    try:
        transactions_obj = Dashboard(user_id=payload.user_id)
        result = transactions_obj.get_transactions()
        return result
    except Exception as e:
        logging.error(f"Error occurred as: {e}")
        raise HTTPException(status_code=500, detail=f'Could not fetch budgets data due to: {e}')


@router.post('/qna')
async def qna(payload: QnARequest):
    try:
        qna_obj = QnA()
        prompt = qna_obj.create_prompt(user_query=payload.user_query, user_id=payload.user_id)
        response = qna_obj.generate_gemini_response(prompt) 
        return response
    except Exception as e:
        logging.error(f"Error occurred as: {e}")
        raise HTTPException(status_code=500, detail=f'Could not fetch response due to: {e}')
