from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from logger import logging

from src.models.dashboard import Dashboard

router = APIRouter(
    prefix='/dashboard',
    tags=['dashboard'])

# ------------------------- Models -------------------------

class UserRequest(BaseModel):
    user_id: str

# ------------------------- Routes -------------------------

@router.post('/')
async def dashboard(payload: UserRequest):
    try:
        dashboard_obj = Dashboard(payload.user_id)
        result = dashboard_obj.total_spending()
        return result
    except Exception as e:
        logging.error(f"Error occurred as: {e}")
        raise HTTPException(status_code=500, detail=f'Could not fetch dashboard data due to: {e}')