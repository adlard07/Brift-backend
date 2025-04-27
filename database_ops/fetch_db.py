import os
import json
from dataclasses import dataclass, field
from firebase_admin import db
from dotenv import load_dotenv

from logger import logging
from database_ops.auth import FirebaseAuth
from database_ops.services import DBServices

# Load environment variables
load_dotenv()

@dataclass
class FetchFirebase:
    auth_client: FirebaseAuth = field(default_factory=FirebaseAuth)
    db_services: DBServices = field(default_factory=DBServices)
    ref: db.Reference = field(init=False)

    def __post_init__(self):
        self.ref = self.auth_client.initialize_firebase_app('user')

    def fetch_user(self, user_id: str) -> dict:
        try:
            data = self.ref.child(user_id).get()
            if not data:
                return {"status_code": 404, "error": "User not found"}
            return {"status_code": 200, "data": data}
        except Exception as e:
            logging.error(f"Error fetching user: {e}")
            return {"status_code": 500, "error": str(e)}

    def fetch_expenses(self, user_id: str) -> dict:
        return self._fetch_child_data(user_id, 'expenses')

    def fetch_budgets(self, user_id: str) -> dict:
        return self._fetch_child_data(user_id, 'budgets')

    def fetch_income(self, user_id: str) -> dict:
        return self._fetch_child_data(user_id, 'incomes')

    def fetch_goals(self, user_id: str) -> dict:
        return self._fetch_child_data(user_id, 'goals')

    def fetch_bills(self, user_id: str) -> dict:
        return self._fetch_child_data(user_id, 'bills')

    def fetch_reminders(self, user_id: str) -> dict:
        return self._fetch_child_data(user_id, 'reminders')

    def fetch_notifications(self, user_id: str) -> dict:
        return self._fetch_child_data(user_id, 'notifications')

    def fetch_debt(self, user_id: str) -> dict:
        return self._fetch_child_data(user_id, 'debts')

    def fetch_investment(self, user_id: str) -> dict:
        return self._fetch_child_data(user_id, 'investments')

    # Helper function to avoid repetition
    def _fetch_child_data(self, user_id: str, child_node: str) -> dict:
        try:
            data = self.ref.child(user_id).child(child_node).get()
            if not data:
                return {"status_code": 404, "error": f"No {child_node} data found for user"}
            return {"status_code": 200, "data": data}
        except Exception as e:
            logging.error(f"Error fetching {child_node}: {e}")
            return {"status_code": 500, "error": str(e)}


if __name__ == "__main__":
    firebase_object = FetchFirebase()
    user_id = 'c3f7bf9a-fe91-4f4e-9be2-ecac74d89acc'

    logging.info(firebase_object.fetch_user(user_id))
    logging.info(firebase_object.fetch_expenses(user_id))
    logging.info(firebase_object.fetch_budgets(user_id))
    logging.info(firebase_object.fetch_income(user_id))
    logging.info(firebase_object.fetch_goals(user_id))
    logging.info(firebase_object.fetch_bills(user_id))
    logging.info(firebase_object.fetch_reminders(user_id))
    logging.info(firebase_object.fetch_notifications(user_id))
    logging.info(firebase_object.fetch_debt(user_id))
    logging.info(firebase_object.fetch_investment(user_id))
