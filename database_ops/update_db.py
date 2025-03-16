import os
import requests
import json
from dataclasses import dataclass
from dotenv import load_dotenv
from datetime import datetime

from logger import logging

load_dotenv()

def check_response(response) -> dict:
    """Checks status_code and returns either data or error"""
    if response.status_code == 200:
        return {"status_code": response.status_code, "data": response.json()}
    else:
        return {"status_code": response.status_code, "error": response.text}

@dataclass
class UpdateFirebase:
    base_url = os.getenv("BASE_URL", "").rstrip("/")

    def update_user(self, user_id: str, username: str = None, email: str = None, password: str = None) -> dict:
        """Updates user information"""
        try:
            update_data = {}
            if username:
                update_data["username"] = username
            if email:
                update_data["email"] = email
            if password:
                update_data["password"] = password

            if not update_data:
                return {"status_code": 400, "error": "No fields provided for update"}

            user_url = f"{self.base_url}/users/{user_id}.json"
            response = requests.patch(user_url, json=update_data)
            return check_response(response)

        except Exception as e:
            logging.error(f"Error updating user: {e}")
            return {"status_code": 500, "error": str(e)}

    def update_expense(self, user_id: str, expense_id: str, title: str = None, category: str = None, amount: float = None, date: str = None, payment_method: str = None) -> dict:
        """Updates an expense"""
        try:
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

            expense_url = f"{self.base_url}/users/{user_id}/expenses/{expense_id}.json"
            response = requests.patch(expense_url, json=update_data)
            return check_response(response)

        except Exception as e:
            logging.error(f"Error updating expense: {e}")
            return {"status_code": 500, "error": str(e)}

    def update_budget(self, user_id: str, budget_id: str, category: str = None, amount: float = None, period_in_days: int = None) -> dict:
        """Updates a budget"""
        try:
            update_data = {}
            if category:
                update_data["category"] = category
            if amount is not None:
                update_data["amount"] = amount
            if period_in_days:
                update_data["period_in_days"] = period_in_days

            if not update_data:
                return {"status_code": 400, "error": "No fields provided for update"}

            budget_url = f"{self.base_url}/users/{user_id}/budgets/{budget_id}.json"
            response = requests.patch(budget_url, json=update_data)
            return check_response(response)

        except Exception as e:
            logging.error(f"Error updating budget: {e}")
            return {"status_code": 500, "error": str(e)}

    def update_income(self, user_id: str, income_id: str, source: str = None, amount: float = None, frequency: str = None) -> dict:
        """Updates an income entry"""
        try:
            update_data = {}
            if source:
                update_data["source"] = source
            if amount is not None:
                update_data["amount"] = amount
            if frequency:
                update_data["frequency"] = frequency

            if not update_data:
                return {"status_code": 400, "error": "No fields provided for update"}

            income_url = f"{self.base_url}/users/{user_id}/income/{income_id}.json"
            response = requests.patch(income_url, json=update_data)
            return check_response(response)

        except Exception as e:
            logging.error(f"Error updating income: {e}")
            return {"status_code": 500, "error": str(e)}

    def update_goal(self, user_id: str, goal_id: str, title: str = None, target_amount: float = None, saved_amount: float = None, status: str = None) -> dict:
        """Updates a financial goal"""
        try:
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

            goal_url = f"{self.base_url}/users/{user_id}/goals/{goal_id}.json"
            response = requests.patch(goal_url, json=update_data)
            return check_response(response)

        except Exception as e:
            logging.error(f"Error updating goal: {e}")
            return {"status_code": 500, "error": str(e)}

    def update_recurring_payment(self, user_id: str, payment_id: str, service_name: str = None, amount: float = None, frequency: str = None, auto_deduct: bool = None) -> dict:
        """Updates a recurring payment"""
        try:
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

            payment_url = f"{self.base_url}/users/{user_id}/recurring_payments/{payment_id}.json"
            response = requests.patch(payment_url, json=update_data)
            return check_response(response)

        except Exception as e:
            logging.error(f"Error updating recurring payment: {e}")
            return {"status_code": 500, "error": str(e)}

    def update_notification(self, user_id: str, notification_id: str, message: str = None, read: bool = None) -> dict:
        """Updates a notification"""
        try:
            update_data = {}
            if message:
                update_data["message"] = message
            if read is not None:
                update_data["read"] = read

            if not update_data:
                return {"status_code": 400, "error": "No fields provided for update"}

            notification_url = f"{self.base_url}/users/{user_id}/notifications/{notification_id}.json"
            response = requests.patch(notification_url, json=update_data)
            return check_response(response)

        except Exception as e:
            logging.error(f"Error updating notification: {e}")
            return {"status_code": 500, "error": str(e)}


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