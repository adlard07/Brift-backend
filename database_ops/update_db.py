import os
import requests
from dataclasses import dataclass
from dotenv import load_dotenv
from datetime import datetime

from logger import logging
from database_ops.auth import FirebaseAuth

load_dotenv()


def check_response(response) -> dict:
    if response.status_code == 200:
        return {"status_code": response.status_code, "data": response.json()}
    else:
        return {"status_code": response.status_code, "error": response.text}


@dataclass(kw_only=True)
class UpdateFirebase:
    base_url: str = os.getenv("BASE_URL", "").rstrip("/")
    auth_client: FirebaseAuth = FirebaseAuth()

    def get_access_token(self):
        return self.auth_client.get_access_token()

    def _patch(self, endpoint: str, data: dict) -> dict:
        """Reusable patch request"""
        access_token = self.get_access_token()
        url = f"{self.base_url}/{endpoint}.json?access_token={access_token}"
        response = requests.patch(url, json=data)
        return check_response(response)

    def update_user(self, user_id: str, username: str = None, email: str = None, 
                    password: str = None) -> dict:
        update_data = {}
        if username:
            update_data["username"] = username
        if email:
            update_data["email"] = email
        if password:
            update_data["password"] = password
        if not update_data:
            return {"status_code": 400, "error": "No fields provided for update"}
        return self._patch(f"users/{user_id}", update_data)

    def update_expense(self, user_id: str, expense_id: str, title: str = None, 
                        category: str = None, amount: float = None, date: str = None, 
                        payment_method: str = None) -> dict:
        update_data = {}
        if title:
            update_data["title"] = title
        if category:
            update_data["category"] = category
        if amount is not None:
            update_data["amount"] = amount
        if date:
            update_data["date"] = date
        if payment_method:
            update_data["payment_method"] = payment_method
        if not update_data:
            return {"status_code": 400, "error": "No fields provided for update"}
        return self._patch(f"users/{user_id}/expenses/{expense_id}", update_data)

    def update_budget(self, user_id: str, budget_id: str, category: str = None, 
                    amount: float = None, period_in_days: int = None) -> dict:
        update_data = {}
        if category:
            update_data["category"] = category
        if amount is not None:
            update_data["amount"] = amount
        if period_in_days:
            update_data["period_in_days"] = period_in_days
        if not update_data:
            return {"status_code": 400, "error": "No fields provided for update"}
        return self._patch(f"users/{user_id}/budgets/{budget_id}", update_data)

    def update_income(self, user_id: str, income_id: str, source: str = None, 
                        amount: float = None, frequency: str = None) -> dict:
        update_data = {}
        if source:
            update_data["source"] = source
        if amount is not None:
            update_data["amount"] = amount
        if frequency:
            update_data["frequency"] = frequency
        if not update_data:
            return {"status_code": 400, "error": "No fields provided for update"}
        return self._patch(f"users/{user_id}/income/{income_id}", update_data)

    def update_goal(self, user_id: str, goal_id: str, title: str = None, 
                    target_amount: float = None, saved_amount: float = None, 
                    status: str = None) -> dict:
        update_data = {}
        if title:
            update_data["title"] = title
        if target_amount is not None:
            update_data["target_amount"] = target_amount
        if saved_amount is not None:
            update_data["saved_amount"] = saved_amount
        if status:
            update_data["status"] = status
        if not update_data:
            return {"status_code": 400, "error": "No fields provided for update"}
        return self._patch(f"users/{user_id}/goals/{goal_id}", update_data)

    def update_recurring_payment(self, user_id: str, payment_id: str, service_name: str = None, 
                                amount: float = None, frequency: str = None, 
                                auto_deduct: bool = None) -> dict:
        update_data = {}
        if service_name:
            update_data["service_name"] = service_name
        if amount is not None:
            update_data["amount"] = amount
        if frequency:
            update_data["frequency"] = frequency
        if auto_deduct is not None:
            update_data["auto_deduct"] = auto_deduct
        if not update_data:
            return {"status_code": 400, "error": "No fields provided for update"}
        return self._patch(f"users/{user_id}/recurring_payments/{payment_id}", update_data)

    def update_notification(self, user_id: str, notification_id: str, message: str = None, 
                            read: bool = None) -> dict:
        update_data = {}
        if message:
            update_data["message"] = message
        if read is not None:
            update_data["read"] = read
        if not update_data:
            return {"status_code": 400, "error": "No fields provided for update"}
        return self._patch(f"users/{user_id}/notifications/{notification_id}", update_data)


if __name__=="__main__":
    firebase_updater = UpdateFirebase()
    user_id = 'af02a499-01b6-11f0-9306-00155d016700'

    # response = firebase_updater.update_user(
    #     user_id="af02a499-01b6-11f0-9306-00155d016700", 
    #     username="adlard")

    # response = firebase_updater.update_expense(
    #     user_id=user_id, 
    #     expense_id='cdd56270-01b6-11f0-bd4a-00155d016700',
    #     category='Food',
    #     title='Biscuits')

    # response = firebase_updater.update_budget(
    #     user_id=user_id,
    #     budget_id='c14697f6-01b6-11f0-9d09-00155d016700',
    #     amount=2000)

    # response = firebase_updater.update_income(
    #     user_id=user_id,
    #     income_id='c19d56b8-01b6-11f0-9501-00155d016700',
    #     amount=33000)

    print(response)