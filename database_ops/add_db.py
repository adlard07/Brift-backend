import os
import requests
import json
from dataclasses import dataclass
from dotenv import load_dotenv
import uuid
from datetime import date, datetime

from logger import logging

# Load environment variables
load_dotenv()

def check_user(email, base_url) -> bool:
    """Checks if user exists"""
    try:
        users = requests.get(f"{base_url}/users.json").json()
        if users is None:
            logging.info('User does not exist.')
            return False

        for user in users.values():
            if user.get('email') == email:
                logging.info('User exists.')
                return True

        logging.info('User does not exist.')
        return False

    except Exception as e:
        logging.error(f"Error checking user: {e}")
        return False

def check_response(response) -> dict:
    """Checks status_code and returns either data or error"""
    if response.status_code == 200:
        return {"status_code": response.status_code, "data": response.json()}
    else:
        return {"status_code": response.status_code, "error": response.text}

@dataclass
class AddFirebase:
    base_url = os.getenv("BASE_URL", "").rstrip("/")


    def create_user(self, username: str, email: str, password: str) -> dict:
        """Creates a new user"""
        try:
            user_data = {
                "username": username,
                "email": email,
                "password": password,
                "created_at": datetime.utcnow().isoformat()
            }

            if not check_user(email, self.base_url):                
                user_url = f"{self.base_url}/users/{str(uuid.uuid1())}.json"
                response = requests.put(user_url, json=user_data)
                return check_response(response)

            return {"status_code": 400, "error": "User already exists"}

        except Exception as e:
            logging.error(f"Error creating user: {e}")
            return {"status_code": 500, "error": str(e)}

    def add_expense(self, user_id: str, title: str, category: str, amount: float, date: str=date.today().isoformat(), payment_method='UPI') -> dict:
        """Adds a new expense"""
        try:
            expense_data = {
                "title": title,
                "category": category,
                "amount": amount,
                "date": date,
                "payment_method": payment_method
            }
            expense_url = f"{self.base_url}/users/{user_id}/expenses/{str(uuid.uuid1())}.json"
            response = requests.put(expense_url, json=expense_data)

            return check_response(response)

        except Exception as e:
            logging.error(f"Error adding expense: {e}")
            return {"status_code": 500, "error": str(e)}

    def add_budget(self, user_id: str, category: str, amount: float, period_in_days: int) -> dict:
        """Adds a new budget"""
        try:
            budget_data = {
                "category": category,
                "amount": amount,
                "period_in_days": period_in_days,
                "created_at": datetime.utcnow().isoformat()
            }
            budget_url = f"{self.base_url}/users/{user_id}/budgets/{str(uuid.uuid1())}.json"
            response = requests.put(budget_url, json=budget_data)
            return check_response(response)

        except Exception as e:
            logging.error(f"Error adding budget: {e}")
            return {"status_code": 500, "error": str(e)}

    def add_income(self, user_id: str, source: str, amount: float, frequency: str, date_received: str = date.today().isoformat()) -> dict:
        """Adds a new income source"""
        try:
            income_data = {
                "source": source,
                "amount": amount,
                "frequency": frequency,
                "date_received": date_received
            }
            income_url = f"{self.base_url}/users/{user_id}/income/{str(uuid.uuid1())}.json"
            response = requests.put(income_url, json=income_data)

            return check_response(response)

        except Exception as e:
            logging.error(f"Error adding income: {e}")
            return {"status_code": 500, "error": str(e)}

    def add_goals(self, user_id: str, title: str, target_amount: float, deadline: str) -> dict:
        """Adds a new financial goal"""
        try:
            goal_data = {
                "title": title,
                "target_amount": target_amount,
                "saved_amount": 0.0,
                "deadline": deadline,
                "status": "In Progress"
            }
            goal_url = f"{self.base_url}/users/{user_id}/goals/{str(uuid.uuid1())}.json"
            response = requests.put(goal_url, json=goal_data)

            return check_response(response)

        except Exception as e:
            logging.error(f"Error adding goal: {e}")
            return {"status_code": 500, "error": str(e)}

    def add_recurring_payments(self, user_id: str, service_name: str, amount: float, payment_date: str, frequency: str, auto_deduct: bool = False) -> dict:
        """Adds a recurring payment"""
        try:
            payment_data = {
                "service_name": service_name,
                "amount": amount,
                "payment_date": payment_date,
                "frequency": frequency,
                "auto_deduct": auto_deduct
            }
            payment_url = f"{self.base_url}/users/{user_id}/recurring_payments/{str(uuid.uuid1())}.json"
            response = requests.put(payment_url, json=payment_data)

            return check_response(response)

        except Exception as e:
            logging.error(f"Error adding recurring payment: {e}")
            return {"status_code": 500, "error": str(e)}

    def add_notification(self, user_id: str, message: str, type: str = "General") -> dict:
        """Adds a new notification"""
        try:
            notification_data = {
                "message": message,
                "type": type,
                "timestamp": datetime.utcnow().isoformat(),
                "read": False
            }
            notification_url = f"{self.base_url}/users/{user_id}/notifications/{str(uuid.uuid1())}.json"
            response = requests.put(notification_url, json=notification_data)

            return check_response(response)

        except Exception as e:
            logging.error(f"Error adding notification: {e}")
            return {"status_code": 500, "error": str(e)}


if __name__ == "__main__":
    firebase_object = AddFirebase()

    result = firebase_object.create_user(
        username='adelard',
        email='adelarddcunha@gmail.com',
        password='adelard',
    )

    user_id = '4cd6cdc9-00f1-11f0-9eed-00155d016700'

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
