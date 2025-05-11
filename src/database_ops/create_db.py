import os
import json 
import uuid
from dataclasses import dataclass, field
from typing import Optional
from dotenv import load_dotenv
from firebase_admin import db

from logger import logging
from src.database_ops.firebase_auth import FirebaseAuth
from src.database_ops.services import Services

# Load environment variables
load_dotenv()

@dataclass
class AddFirebase:
    auth_client: FirebaseAuth = field(default_factory=FirebaseAuth)
    db_services: Services = field(default_factory=Services)
    ref: db.Reference = field(init=False)

    def __post_init__(self):
        self.ref = self.auth_client.initialize_firebase_app()
        self.db_services.ref = self.ref

    def create_user(self, profile: dict, settings: dict) -> dict:
        try:
            if not profile or not settings:
                return {"status_code": 400, "error": "User data is incomplete."}

            # Check if user with same email/phone exists
            existing_email = bool(self.db_services.fetch_user_by_field(field_name='profile/email', value=profile['email']))
            existing_phone = bool(self.db_services.fetch_user_by_field(field_name='profile/phone', value=profile['phone']))
            if existing_email or existing_phone:
                return {"status_code": 400, "error": "User already exists."}

            profile['password'] = self.db_services.encrypt_text(profile['password'])
            if profile['phone']:
                profile['mfa_enabled'] = True

            combined_data = {"profile": profile, "settings": settings}
            if not combined_data:
                return {"status_code": 500, "error": "Failed to create user."}

            user_id = str(uuid.uuid4())
            self.ref.child(user_id).set(combined_data)

            logging.info(f"User {user_id} created successfully.")
            return {"status_code": 201, "message": "User created successfully", "user_id": user_id}

        except Exception as e:
            logging.error(f"Error creating user: {e}")
            return {"status_code": 500, "error": f"Internal server error: {str(e)}"}


    def add_expense(self, expense):
        return self._add_item(expense['user_id'], 'expenses', expense)
        

    def _add_item(self, user_id: str, node_name: str, data: dict) -> dict:
        try:
            if not user_id:
                return {"status_code": 404, "error": "User ID is missing."}

            item_id = str(uuid.uuid4())
            self.ref.child(user_id).child(node_name).child(item_id).set(data)

            return {
                "status_code": 201,
                "message": f"{node_name.capitalize()} added for user {user_id}",
                "id": item_id
            }
        except Exception as e:
            logging.error(f"Error adding {node_name}: {e}")
            return {"status_code": 500, "error": str(e)}


    def _check_duplicate_by_field(self, user_id: str, node: str, field: str, value: str) -> bool:
        try:
            items = self.ref.child(user_id).child(node).get() or {}
            return any(item.get(field) == value for item in items.values())
        except Exception as e:
            logging.error(f"Error checking duplicate in {node}: {e}")
            return False

    def add_budget(self, budget: dict) -> dict:
        if self._check_duplicate_by_field(budget['user_id'], 'budgets', 'category', budget['category']):
            return {"status_code": 400, "error": "Budget already exists."}
        return self._add_item(budget['user_id'], 'budgets', budget)

    def add_income(self, income: dict) -> dict:
        if self._check_duplicate_by_field(income['user_id'], 'incomes', 'title', income['title']):
            return {"status_code": 400, "error": "Income title already exists."}
        return self._add_item(income['user_id'], 'incomes', income)

    def add_goal(self, goal: dict) -> dict:
        if self._check_duplicate_by_field(goal['user_id'], 'goals', 'title', goal['title']):
            return {"status_code": 400, "error": "Goal already exists."}
        return self._add_item(goal['user_id'], 'goals', goal)

    def add_bill(self, bill: dict) -> dict:
        if self._check_duplicate_by_field(bill['user_id'], 'bills', 'title', bill['title']):
            return {"status_code": 400, "error": "Bill already exists."}
        return self._add_item(bill['user_id'], 'bills', bill)

    def add_reminder(self, reminder: dict) -> dict:
        if self._check_duplicate_by_field(reminder['user_id'], 'reminders', 'title', reminder['title']):
            return {"status_code": 400, "error": "Reminder already exists."}
        return self._add_item(reminder['user_id'], 'reminders', reminder)

    def add_notification(self, notification: dict) -> dict:
        if self._check_duplicate_by_field(notification['user_id'], 'notifications', 'message', notification['message']):
            return {"status_code": 400, "error": "Notification already exists."}
        return self._add_item(notification['user_id'], 'notifications', notification)

    def add_debt(self, debt: dict) -> dict:
        if self._check_duplicate_by_field(debt['user_id'], 'debts', 'title', debt['title']):
            return {"status_code": 400, "error": "Debt already exists."}
        return self._add_item(debt['user_id'], 'debts', debt)

    def add_investment(self, investment: dict) -> dict:
        if self._check_duplicate_by_field(investment['user_id'], 'investments', 'title', investment['title']):
            return {"status_code": 400, "error": "Investment already exists."}
        return self._add_item(investment['user_id'], 'investments', investment)
