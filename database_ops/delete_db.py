import os
import requests
from dataclasses import dataclass
from dotenv import load_dotenv

from logger import logging
from database_ops.auth import FirebaseAuth

# Load environment variables
load_dotenv()

def check_response(response) -> dict:
    """Checks status_code and returns success or error message"""
    if response.status_code == 200:
        return {"status_code": response.status_code, "message": "Deletion successful"}
    else:
        return {"status_code": response.status_code, "error": response.text}


@dataclass
class DeleteFirebase:
    base_url: str = os.getenv("BASE_URL", "").rstrip("/")
    auth_client: FirebaseAuth = FirebaseAuth()

    def get_access_token(self):
        return self.auth_client.get_firebase_access_token()

    def _delete(self, endpoint: str) -> dict:
        """Reusable delete request"""
        access_token = self.get_access_token()
        url = f"{self.base_url}/{endpoint}.json?access_token={access_token}"
        response = requests.delete(url)
        return check_response(response)

    def delete_user(self, user_id: str) -> dict:
        return self._delete(f"users/{user_id}")

    def delete_expense(self, user_id: str, expense_id: str) -> dict:
        return self._delete(f"users/{user_id}/expenses/{expense_id}")

    def delete_budget(self, user_id: str, budget_id: str) -> dict:
        return self._delete(f"users/{user_id}/budgets/{budget_id}")

    def delete_income(self, user_id: str, income_id: str) -> dict:
        return self._delete(f"users/{user_id}/income/{income_id}")

    def delete_goal(self, user_id: str, goal_id: str) -> dict:
        return self._delete(f"users/{user_id}/goals/{goal_id}")

    def delete_recurring_payment(self, user_id: str, payment_id: str) -> dict:
        return self._delete(f"users/{user_id}/recurring_payments/{payment_id}")

    def delete_notification(self, user_id: str, notification_id: str) -> dict:
        return self._delete(f"users/{user_id}/notifications/{notification_id}")



if __name__=="__main__":

    firebase_deleter = DeleteFirebase()
    user_id = '26236395-01c1-11f0-b33c-00155d016700'

    # Delete a specific expense
    response = firebase_deleter.delete_expense(
        user_id=user_id, 
        expense_id="36684e39-01c1-11f0-a0ea-00155d016700")
    print(response)

    # Delete a budget
    response = firebase_deleter.delete_budget(
        user_id=user_id, 
        budget_id="36c04c2a-01c1-11f0-83ad-00155d016700")
    print(response)

    # Delete an income entry
    response = firebase_deleter.delete_income(
        user_id=user_id, 
        income_id="3717c35a-01c1-11f0-af25-00155d016700")
    print(response)

    # Delete a financial goal
    response = firebase_deleter.delete_goal(
        user_id=user_id, 
        goal_id="376e8764-01c1-11f0-82ba-00155d016700")
    print(response)

    # Delete a recurring payment
    response = firebase_deleter.delete_recurring_payment(
        user_id=user_id, 
        payment_id="37c744ae-01c1-11f0-ae46-00155d016700")
    print(response)

    # Delete a notification
    response = firebase_deleter.delete_notification(
        user_id=user_id, 
        notification_id="381d4395-01c1-11f0-8af4-00155d016700")
    print(response)

    # Delete a user
    response = firebase_deleter.delete_user(
        user_id=user_id)
    print(response)