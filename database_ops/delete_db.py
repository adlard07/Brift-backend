import os
import requests
from dataclasses import dataclass
from dotenv import load_dotenv

from logger import logging

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
    base_url = os.getenv("BASE_URL", "").rstrip("/")

    def delete_user(self, user_id: str) -> dict:
        """Deletes a user and all their associated data"""
        try:
            user_url = f"{self.base_url}/users/{user_id}.json"
            response = requests.delete(user_url)
            return check_response(response)

        except Exception as e:
            logging.error(f"Error deleting user: {e}")
            return {"status_code": 500, "error": str(e)}

    def delete_expense(self, user_id: str, expense_id: str) -> dict:
        """Deletes a specific expense for a user"""
        try:
            expense_url = f"{self.base_url}/users/{user_id}/expenses/{expense_id}.json"
            response = requests.delete(expense_url)
            return check_response(response)

        except Exception as e:
            logging.error(f"Error deleting expense: {e}")
            return {"status_code": 500, "error": str(e)}

    def delete_budget(self, user_id: str, budget_id: str) -> dict:
        """Deletes a specific budget for a user"""
        try:
            budget_url = f"{self.base_url}/users/{user_id}/budgets/{budget_id}.json"
            response = requests.delete(budget_url)
            return check_response(response)

        except Exception as e:
            logging.error(f"Error deleting budget: {e}")
            return {"status_code": 500, "error": str(e)}

    def delete_income(self, user_id: str, income_id: str) -> dict:
        """Deletes a specific income entry for a user"""
        try:
            income_url = f"{self.base_url}/users/{user_id}/income/{income_id}.json"
            response = requests.delete(income_url)
            return check_response(response)

        except Exception as e:
            logging.error(f"Error deleting income: {e}")
            return {"status_code": 500, "error": str(e)}

    def delete_goal(self, user_id: str, goal_id: str) -> dict:
        """Deletes a specific financial goal for a user"""
        try:
            goal_url = f"{self.base_url}/users/{user_id}/goals/{goal_id}.json"
            response = requests.delete(goal_url)
            return check_response(response)

        except Exception as e:
            logging.error(f"Error deleting goal: {e}")
            return {"status_code": 500, "error": str(e)}

    def delete_recurring_payment(self, user_id: str, payment_id: str) -> dict:
        """Deletes a specific recurring payment for a user"""
        try:
            payment_url = f"{self.base_url}/users/{user_id}/recurring_payments/{payment_id}.json"
            response = requests.delete(payment_url)
            return check_response(response)

        except Exception as e:
            logging.error(f"Error deleting recurring payment: {e}")
            return {"status_code": 500, "error": str(e)}

    def delete_notification(self, user_id: str, notification_id: str) -> dict:
        """Deletes a specific notification for a user"""
        try:
            notification_url = f"{self.base_url}/users/{user_id}/notifications/{notification_id}.json"
            response = requests.delete(notification_url)
            return check_response(response)

        except Exception as e:
            logging.error(f"Error deleting notification: {e}")
            return {"status_code": 500, "error": str(e)}


firebase_deleter = DeleteFirebase()

# Delete a user
response = firebase_deleter.delete_user(user_id="12345")
print(response)

# Delete a specific expense
response = firebase_deleter.delete_expense(user_id="12345", expense_id="67890")
print(response)

# Delete a budget
response = firebase_deleter.delete_budget(user_id="12345", budget_id="abcde")
print(response)

# Delete an income entry
response = firebase_deleter.delete_income(user_id="12345", income_id="98765")
print(response)

# Delete a financial goal
response = firebase_deleter.delete_goal(user_id="12345", goal_id="fghij")
print(response)

# Delete a recurring payment
response = firebase_deleter.delete_recurring_payment(user_id="12345", payment_id="klmno")
print(response)

# Delete a notification
response = firebase_deleter.delete_notification(user_id="12345", notification_id="pqrst")
print(response)
