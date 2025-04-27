import os
import uuid
import json
from datetime import date, datetime
from typing import Optional

import firebase_admin
from firebase_admin import credentials, db
from dataclasses import dataclass, field
from dotenv import load_dotenv

from logger import logging
from database_ops.auth import FirebaseAuth
from database_ops.services import DBServices


# Load environment variables
load_dotenv()


@dataclass
class AddFirebase:
    auth_client: FirebaseAuth = field(default_factory=FirebaseAuth)
    db_services: DBServices = field(default_factory=DBServices)
    ref: db.Reference = field(init=False)


    def __post_init__(self):
        self.ref = self.auth_client.initialize_firebase_app('user')


    def create_user(self, profile: dict, settings: dict) -> dict:
        """Creates a new user if email and phone are unique."""
        try:
            logging.info(f"Profile: {profile}")
            logging.info(f"Settings: {settings}")

            if not profile or not settings:
                return {"error": "User data is incomplete.", "status_code": 400}

            # Check if user with same email exists
            existing_email = self.db_services.fetch_user_by_field(field_name='profile/email', value=profile['email'], ref=self.user_ref)
            if existing_email and isinstance(existing_email, dict) and len(existing_email) > 0:
                return {"status_code": 400, "error": "User email already exists."}

            # Check if user with same phone exists
            existing_phone = self.db_services.fetch_user_by_field(field_name='profile/phone', value=profile['phone'], ref=self.user_ref)
            if existing_phone and isinstance(existing_phone, dict) and len(existing_phone) > 0:
                return {"status_code": 400, "error": "User phone already exists."}

            user_id = str(uuid.uuid4())
            user_data = {
                "profile": profile,
                "settings": settings
            }

            self.ref.child(user_id).set(user_data)

            return {
                "status_code": 201,
                "message": "User created successfully",
                "user_id": user_id
            }

        except Exception as e:
            logging.error(f"Error creating user: {e}")
            return {"status_code": 500, "error": f"Internal server error: {str(e)}"}



    def add_expense(self, expense: dict) -> dict:
        """Adds an expense record to the given user's Firebase entry."""
        try:
            user_id = expense['user_id']
            if not user_id:
                return {"status_code": 404, "error": "User not found"}

            expense_id = str(uuid.uuid4())
            self.ref.child(user_id).child("expenses").child(expense_id).set(expense)

            return {
                "status_code": 201,
                "message": f"Expense added for user {user_id}",
                "expense_id": expense_id
            }

        except Exception as e:
            logging.error(f"Error adding expense: {e}")
            return {"status_code": 500, "error": str(e)}


    def add_budget(self, budget: dict) -> dict:
        try:
            user_id = budget['user_id']
            if not user_id:
                return {"status_code": 404, "error": "User not found"}

            budget_id = str(uuid.uuid4())

            self.ref.child(user_id).child("budgets").child(budget_id).set(budget)

            return {
                "status_code": 201,
                "message": f"Budget added for user {user_id}",
                "budget_id": budget_id
            }

        except Exception as e:
            logging.error(f"Error adding budget: {e}")
            return {"status_code": 500, "error": str(e)}



    def add_income(self, income) -> dict:
        try:
            user_id = income['user_id']
            if not user_id:
                return {"status_code": 404, "error": "User not found"}

            income_id = str(uuid.uuid4())

            self.ref.child(user_id).child("incomes").child(income_id).set(income)

            return {
                "status_code": 201,
                "message": f"Income added for user {user_id}",
                "income_id": income_id
            }

        except Exception as e:
            logging.error(f"Error adding income: {e}")
            return {"status_code": 500, "error": str(e)}



    def add_goals(self, goal: dict) -> dict:
        try:
            user_id = goal['user_id']
            if not user_id:
                return {"status_code": 404, "error": "User not found"}

            goal_id = str(uuid.uuid4())

            self.ref.child(user_id).child("goals").child(goal_id).set(goal)

            return {
                "status_code": 201,
                "message": f"Goal added for user {user_id}",
                "goal_id": goal_id
            }

        except Exception as e:
            logging.error(f"Error adding goal: {e}")
            return {"status_code": 500, "error": str(e)}



    def add_bill(self, bill: dict) -> dict:
        try:
            user_id = bill['user_id']
            if not user_id:
                return {"status_code": 404, "error": "User not found"}

            bill_id = str(uuid.uuid4())

            self.ref.child(user_id).child("bills").child(bill_id).set(bill)

            return {
                "status_code": 201,
                "message": f"Bill added for user {user_id}",
                "bill_id": bill_id
            }

        except Exception as e:
            logging.error(f"Error adding bill: {e}")
            return {"status_code": 500, "error": str(e)}



    def add_reminder(self, reminder: dict) -> dict:
        try:
            user_id = reminder['user_id']
            if not user_id:
                return {"status_code": 404, "error": "User not found"}

            reminder_id = str(uuid.uuid4())

            self.ref.child(user_id).child("reminders").child(reminder_id).set(reminder)

            return {
                "status_code": 201,
                "message": f"Reminder added for user {user_id}",
                "reminder_id": reminder_id
            }

        except Exception as e:
            logging.error(f"Error adding reminder: {e}")
            return {"status_code": 500, "error": str(e)}



    def add_notification(self, notification: dict) -> dict:
        try:
            user_id = notification['user_id']
            if not user_id:
                return {"status_code": 404, "error": "User not found"}

            notification_id = str(uuid.uuid4())

            self.ref.child(user_id).child("notifications").child(notification_id).set(notification)

            return {
                "status_code": 201,
                "message": f"Notification added for user {user_id}",
                "notification_id": notification_id
            }

        except Exception as e:
            logging.error(f"Error adding notification: {e}")
            return {"status_code": 500, "error": str(e)}



    def add_debt(self, debt: dict) -> dict:
        try:
            user_id = debt['user_id']
            if not user_id:
                return {"status_code": 404, "error": "User not found"}

            debt_id = str(uuid.uuid4())

            self.ref.child(user_id).child("debts").child(debt_id).set(debt)

            return {
                "status_code": 201,
                "message": f"Debt added for user {user_id}",
                "debt_id": debt_id
            }

        except Exception as e:
            logging.error(f"Error adding debt: {e}")
            return {"status_code": 500, "error": str(e)}



    def add_investment(self, investment: dict) -> dict:
        try:
            user_id = investment['user_id']
            if not user_id:
                return {"status_code": 404, "error": "User not found"}

            investment_id = str(uuid.uuid4())

            self.ref.child(user_id).child("investments").child(investment_id).set(investment)

            return {
                "status_code": 201,
                "message": f"Investment added for user {user_id}",
                "investment_id": investment_id
            }

        except Exception as e:
            logging.error(f"Error adding investment: {e}")
            return {"status_code": 500, "error": str(e)}
