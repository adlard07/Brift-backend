import os
import requests
import json
from dotenv import load_dotenv
import uuid
from datetime import date, datetime

from logger import logging
from database_ops.auth import FirebaseAuth

# Load environment variables
load_dotenv()

def check_response(response) -> dict:
    if response.status_code == 200:
        return {"status_code": response.status_code, "data": response.json()}
    else:
        return {"status_code": response.status_code, "error": response.text}

class AddFirebase:
    base_url: str = os.getenv("BASE_URL", "").rstrip("/")
    auth_client: FirebaseAuth = FirebaseAuth()

    def get_access_token(self):
        return self.auth_client.get_access_token()

    def _put(self, endpoint: str, data: dict) -> dict:
        """Reusable PUT request"""
        access_token = self.get_access_token()
        url = f"{self.base_url}/{endpoint}.json?access_token={access_token}"
        response = requests.put(url, json=data)
        return check_response(response)

    def check_user(self, email) -> bool:
        """Checks if user exists"""
        try:
            access_token = self.get_access_token()
            check_user_url = f"{self.base_url}/users.json?access_token={access_token}"
            users = requests.get(check_user_url).json()
            if users is None:
                logging.info('User does not exist.')
                return False
            for user in users.values():
                if isinstance(user, dict) and user.get('email') == email:
                    logging.info('User exists.')
                    return True
            logging.info('User does not exist.')
            return False
        except Exception as e:
            logging.error(f"Error checking user: {e}")
            return False

    def create_user(self, username: str, email: str, phone: str, password: str) -> dict:
        """Creates a new user"""
        try:
            user_data = {
                "username": username,
                "email": email,
                "phone": phone,
                "password": password,
                "created_at": datetime.utcnow().isoformat()
            }
            if not self.check_user(email):
                return self._put(f"users/{str(uuid.uuid1())}", user_data)
            return {"status_code": 400, "error": "User already exists"}
        except Exception as e:
            logging.error(f"Error creating user: {e}")
            return {"status_code": 500, "error": str(e)}

    def add_expense(self, user_id: str, title: str, category: str, amount: float, 
                    date: str = date.today().isoformat(), payment_method='UPI') -> dict:
        expense_data = {
            "title": title,
            "category": category,
            "amount": amount,
            "date": date,
            "payment_method": payment_method
        }
        return self._put(f"users/{user_id}/expenses/{str(uuid.uuid1())}", expense_data)

    def add_budget(self, user_id: str, category: str, amount: float, period_in_days: int) -> dict:
        budget_data = {
            "category": category,
            "amount": amount,
            "period_in_days": period_in_days,
            "created_at": datetime.utcnow().isoformat()
        }
        return self._put(f"users/{user_id}/budgets/{str(uuid.uuid1())}", budget_data)

    def add_income(self, user_id: str, source: str, amount: float, frequency: str,
                   date_received: str = date.today().isoformat()) -> dict:
        income_data = {
            "source": source,
            "amount": amount,
            "frequency": frequency,
            "date_received": date_received
        }
        return self._put(f"users/{user_id}/income/{str(uuid.uuid1())}", income_data)

    def add_goals(self, user_id: str, title: str, target_amount: float, deadline: str) -> dict:
        goal_data = {
            "title": title,
            "target_amount": target_amount,
            "saved_amount": 0.0,
            "deadline": deadline,
            "status": "In Progress"
        }
        return self._put(f"users/{user_id}/goals/{str(uuid.uuid1())}", goal_data)

    def add_recurring_payments(self, user_id: str, service_name: str, 
                                amount: float, payment_date: str, frequency: str, 
                                auto_deduct: bool = False) -> dict:
        payment_data = {
            "service_name": service_name,
            "amount": amount,
            "payment_date": payment_date,
            "frequency": frequency,
            "auto_deduct": auto_deduct
        }
        return self._put(f"users/{user_id}/recurring_payments/{str(uuid.uuid1())}", payment_data)

    def add_notification(self, user_id: str, message: str, type: str = "General") -> dict:
        notification_data = {
            "message": message,
            "type": type,
            "timestamp": datetime.utcnow().isoformat(),
            "read": False
        }
        return self._put(f"users/{user_id}/notifications/{str(uuid.uuid1())}", notification_data)


if __name__ == "__main__":
    firebase_object = AddFirebase()

    result = firebase_object.create_user(
        username='albina',
        email='albinadcuna1970@gmail.com',
        phone='+919619886892',
        password='albina',
    )

    user_id = 'f985826d-021f-11f0-ada1-00155d92ba78'

    # Add Expense
    result = firebase_object.add_expense(
        user_id=user_id,
        title="Lunch",
        category="Food",
        amount=250
    )
    logging.info(result)

    # Add Budget
    result = firebase_object.add_budget(
        user_id=user_id,
        category="Groceries",
        amount=5000,
        period_in_days=30
    )
    logging.info(result)

    # Add Income
    result = firebase_object.add_income(
        user_id=user_id,
        source="Freelance Work",
        amount=25000,
        frequency="Monthly"
    )
    logging.info(result)

    # Add Goal
    result = firebase_object.add_goals(
        user_id=user_id,
        title="New Laptop",
        target_amount=80000,
        deadline="2025-12-31"
    )
    logging.info(result)

    # Add Recurring Payment
    result = firebase_object.add_recurring_payments(
        user_id=user_id,
        service_name="Netflix Subscription",
        amount=500,
        payment_date="2025-03-20",
        frequency="Monthly",
        auto_deduct=True
    )
    logging.info(result)

    # Add Notification
    result = firebase_object.add_notification(
        user_id=user_id,
        message="Budget alert! You’ve spent 80% of your Food budget."
    )
    logging.info(result)
