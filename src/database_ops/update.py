import os
from dataclasses import dataclass, field
from dotenv import load_dotenv
from datetime import datetime
from firebase_admin import db
from typing import Optional

from logger import logging
from src.database_ops.firebase_auth import FirebaseAuth
from src.database_ops.services import Services

load_dotenv()

@dataclass
class UpdateFirebase:
    auth_client: FirebaseAuth = field(default_factory=FirebaseAuth)
    db_services: Services = field(default_factory=Services)
    ref: db.Reference = field(init=False)

    def __post_init__(self):
        self.ref = self.auth_client.initialize_firebase_app()

    def _update(self, path: str, data: dict) -> dict:
        try:
            self.ref.child(path).update(data)
            return {"status_code": 200, "message": "Update successful"}
        except Exception as e:
            logging.error(f"Update error at path '{path}': {e}")
            return {"status_code": 500, "error": str(e)}

    def _prepare_update_data(self, **fields) -> dict:
        update_data = {key: value for key, value in fields.items() if value is not None}
        if not update_data:
            return {"status_code": 400, "error": "No fields provided for update"}
        return update_data

    def update_user(self, user_id: str, username: str = None, password: str = None) -> dict:
        update_data = self._prepare_update_data(username=username, password=password)
        if "error" in update_data:
            return update_data
        return self._update(f"{user_id}", update_data)

    def update_expense(self, user_id: str, expense_id: str, title: str = None,
                       category: str = None, amount: float = None,
                       date: str = None, payment_method: str = None) -> dict:
        update_data = self._prepare_update_data(title=title, category=category, amount=amount, date=date, payment_method=payment_method)
        if "error" in update_data:
            return update_data
        return self._update(f"{user_id}/expenses/{expense_id}", update_data)

    def update_budget(self, user_id: str, budget_id: str, category: str = None,
                      amount: float = None, period_in_days: int = None) -> dict:
        update_data = self._prepare_update_data(category=category, amount=amount, period_in_days=period_in_days)
        if "error" in update_data:
            return update_data
        return self._update(f"{user_id}/budgets/{budget_id}", update_data)

    def update_income(self, user_id: str, income_id: str, source: str = None,
                      amount: float = None, frequency: str = None) -> dict:
        update_data = self._prepare_update_data(source=source, amount=amount, frequency=frequency)
        if "error" in update_data:
            return update_data
        return self._update(f"{user_id}/income/{income_id}", update_data)

    def update_goal(self, user_id: str, goal_id: str, title: str = None,
                    target_amount: float = None, saved_amount: float = None,
                    status: str = None) -> dict:
        update_data = self._prepare_update_data(title=title, target_amount=target_amount, saved_amount=saved_amount, status=status)
        if "error" in update_data:
            return update_data
        return self._update(f"{user_id}/goals/{goal_id}", update_data)

    def update_notification(self, user_id: str, notification_id: str, message: str = None,
                             read: bool = None) -> dict:
        update_data = self._prepare_update_data(message=message, read=read)
        if "error" in update_data:
            return update_data
        return self._update(f"{user_id}/notifications/{notification_id}", update_data)

    def update_recurring_payment(self, user_id: str, payment_id: str, service_name: str = None,
                                  amount: float = None, frequency: str = None,
                                  auto_deduct: bool = None) -> dict:
        update_data = self._prepare_update_data(service_name=service_name, amount=amount, frequency=frequency, auto_deduct=auto_deduct)
        if "error" in update_data:
            return update_data
        return self._update(f"{user_id}/recurring_payments/{payment_id}", update_data)


if __name__ == "__main__":
    firebase_updater = UpdateFirebase()
    user_id = 'c3f7bf9a-fe91-4f4e-9be2-ecac74d89acc'

    response = firebase_updater.update_goal(
        user_id=user_id,
        goal_id='882aa0ac-19b6-4a81-a092-5de1eaf8c46a',
        saved_amount=5000,
        status='On Track'
    )

    logging.info(response)
