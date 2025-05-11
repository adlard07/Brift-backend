import os
import requests
from dataclasses import dataclass, field
from dotenv import load_dotenv
from firebase_admin import credentials, db

from logger import logging
from src.database_ops.firebase_auth import FirebaseAuth
from src.database_ops.services import Services

@dataclass
class DeleteFirebase:
    auth_client: FirebaseAuth = field(default_factory=FirebaseAuth)
    db_services: Services = field(default_factory=Services)
    ref: db.Reference = field(init=False)

    def __post_init__(self):
        self.ref = self.auth_client.initialize_firebase_app()

    def _delete(self, path: str):
        try:
            logging.info(f"Deleting path: {path}")
            return self.ref.child(path).delete()
        except Exception as e:
            logging.error(f"Failed to delete path: {path} - Error: {e}")
            return {"error": str(e)}

    def delete_user(self, user_id: str) -> dict:
        return self._delete(f"{user_id}")

    def delete_expense(self, user_id: str, expense_id: str) -> dict:
        return self._delete(f"{user_id}/expenses/{expense_id}")

    def delete_budget(self, user_id: str, budget_id: str) -> dict:
        return self._delete(f"{user_id}/budgets/{budget_id}")

    def delete_income(self, user_id: str, income_id: str) -> dict:
        return self._delete(f"{user_id}/income/{income_id}")

    def delete_goal(self, user_id: str, goal_id: str) -> dict:
        return self._delete(f"{user_id}/goals/{goal_id}")

    def delete_notification(self, user_id: str, notification_id: str) -> dict:
        return self._delete(f"{user_id}/notifications/{notification_id}")

    def delete_recurring_payment(self, user_id: str, payment_id: str) -> dict:
        return self._delete(f"{user_id}/recurring_payments/{payment_id}")



if __name__ == "__main__":
    firebase_deleter = DeleteFirebase()
    user_id = 'c3f7bf9a-fe91-4f4e-9be2-ecac74d89acc'

    print(firebase_deleter.delete_expense(user_id, "85a1ea2c-1262-4a75-881a-52aa463032a4"))
    # print(firebase_deleter.delete_budget(email, "36c04c2a-01c1-11f0-83ad-00155d016700"))
    # print(firebase_deleter.delete_income(email, "3717c35a-01c1-11f0-af25-00155d016700"))
    # print(firebase_deleter.delete_goal(email, "376e8764-01c1-11f0-82ba-00155d016700"))
    # print(firebase_deleter.delete_recurring_payment(email, "37c744ae-01c1-11f0-ae46-00155d016700"))
    # print(firebase_deleter.delete_notification(email, "381d4395-01c1-11f0-8af4-00155d016700"))
    # print(firebase_deleter.delete_user(email))
