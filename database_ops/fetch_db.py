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

class FetchFirebase:
    base_url: str = os.getenv("BASE_URL", "").rstrip("/")
    auth_client: FirebaseAuth = FirebaseAuth()

    def get_access_token(self):
        return self.auth_client.get_firebase_access_token()

    def _get(self, endpoint: str) -> dict:
        """Reusable GET request"""
        access_token = self.get_access_token()
        url = f"{self.base_url}/users/{endpoint}.json?access_token={access_token}"
        response = requests.get(url)
        return check_response(response)


    def fetch_user(self, user_id: str) -> dict:
        """Fetch user data"""
        return self._get(f"{user_id}")

    def fetch_expenses(self, user_id: str) -> dict:
        """Fetch all expenses for a user"""
        return self._get(f"{user_id}/expenses")

    def fetch_budgets(self, user_id: str) -> dict:
        """Fetch all budgets for a user"""
        return self._get(f"{user_id}/budgets")

    def fetch_income(self, user_id: str) -> dict:
        """Fetch all incomes for a user"""
        return self._get(f"{user_id}/income")

    def fetch_goals(self, user_id: str) -> dict:
        """Fetch all goals for a user"""
        return self._get(f"{user_id}/goals")

    def fetch_recurring_payments(self, user_id: str) -> dict:
        """Fetch all recurring payments for a user"""
        return self._get(f"{user_id}/recurring_payments")

    def fetch_notifications(self, user_id: str) -> dict:
        """Fetch all notifications for a user"""
        return self._get(f"{user_id}/notifications")



if __name__ == "__main__":
    firebase_object = FetchFirebase()

    user_id = 'f985826d-021f-11f0-ada1-00155d92ba78'

    # Fetch User Info
    result = firebase_object.fetch_user(user_id)
    logging.info(result)

    # Fetch Expenses
    result = firebase_object.fetch_expenses(user_id)
    logging.info(result)

    # Fetch Budgets
    result = firebase_object.fetch_budgets(user_id)
    logging.info(result)

    # Fetch Incomes
    result = firebase_object.fetch_income(user_id)
    logging.info(result)

    # Fetch Goals
    result = firebase_object.fetch_goals(user_id)
    logging.info(result)

    # Fetch Recurring Payments
    result = firebase_object.fetch_recurring_payments(user_id)
    logging.info(result)

    # Fetch Notifications
    result = firebase_object.fetch_notifications(user_id)
    logging.info(result)
