import os
from dataclasses import dataclass, field
from dotenv import load_dotenv
from datetime import datetime

from firebase_admin import db
from logger import logging
from database_ops.auth import FirebaseAuth
from database_ops.services import DBServices

load_dotenv()

@dataclass
class UpdateFirebase:
    auth_client: FirebaseAuth = field(default_factory=FirebaseAuth)
    db_services: DBServices = field(default_factory=DBServices)
    ref: db.Reference = field(init=False)

    def __post_init__(self):
        self.user_ref = self.auth_client.initialize_firebase_app('user')
        self.expense_ref = self.auth_client.initialize_firebase_app('expense')
        self.budget_ref = self.auth_client.initialize_firebase_app('budget')
        self.income_ref = self.auth_client.initialize_firebase_app('income')
        self.goal_ref = self.auth_client.initialize_firebase_app('goal')
        self.bill_ref = self.auth_client.initialize_firebase_app('bill')
        self.reminder_ref = self.auth_client.initialize_firebase_app('reminder')
        self.notification_ref = self.auth_client.initialize_firebase_app('notification')
        self.debt_ref = self.auth_client.initialize_firebase_app('debt')
        self.investment_ref = self.auth_client.initialize_firebase_app('investment')


    def _update(self, path: str, data: dict) -> dict:
        try:
            self.ref.child(path).update(data)
            return {"status_code": 200, "message": "Update successful"}
        except Exception as e:
            logging.error(f"Update error at path '{path}': {e}")
            return {"status_code": 500, "error": str(e)}

    def update_user(self, email: str, username: str = None, password: str = None) -> dict:
        update_data = {}
        if username:
            update_data["username"] = username
        if password:
            update_data["password"] = password
        if not update_data:
            return {"status_code": 400, "error": "No fields provided for update"}
        return self._update(email, update_data)

    def update_expense(self, email: str, expense_id: str, title: str = None,
                       category: str = None, amount: float = None,
                       date: str = None, payment_method: str = None) -> dict:
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
        return self._update(f"{email}/expenses/{expense_id}", update_data)

    def update_budget(self, email: str, budget_id: str, category: str = None,
                      amount: float = None, period_in_days: int = None) -> dict:
        update_data = {}
        if category:
            update_data["category"] = category
        if amount is not None:
            update_data["amount"] = amount
        if period_in_days is not None:
            update_data["period_in_days"] = period_in_days
        if not update_data:
            return {"status_code": 400, "error": "No fields provided for update"}
        return self._update(f"{email}/budgets/{budget_id}", update_data)

    def update_income(self, email: str, income_id: str, source: str = None,
                      amount: float = None, frequency: str = None) -> dict:
        update_data = {}
        if source:
            update_data["source"] = source
        if amount is not None:
            update_data["amount"] = amount
        if frequency:
            update_data["frequency"] = frequency
        if not update_data:
            return {"status_code": 400, "error": "No fields provided for update"}
        return self._update(f"{email}/income/{income_id}", update_data)

    def update_goal(self, email: str, goal_id: str, title: str = None,
                    target_amount: float = None, saved_amount: float = None,
                    status: str = None) -> dict:
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
        return self._update(f"{email}/goals/{goal_id}", update_data)

    def update_notification(self, email: str, notification_id: str, message: str = None,
                            read: bool = None) -> dict:
        update_data = {}
        if message:
            update_data["message"] = message
        if read is not None:
            update_data["read"] = read
        if not update_data:
            return {"status_code": 400, "error": "No fields provided for update"}
        return self._update(f"{email}/notifications/{notification_id}", update_data)

    def update_recurring_payment(self, email: str, payment_id: str, service_name: str = None,
                                 amount: float = None, frequency: str = None,
                                 auto_deduct: bool = None) -> dict:
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
        return self._update(f"{email}/recurring_payments/{payment_id}", update_data)


if __name__ == "__main__":
    firebase_updater = UpdateFirebase()
    email = 'albinadcunha1970@gmail.com'

    response = firebase_updater.update_goal(
        email=email,
        goal_id='882aa0ac-19b6-4a81-a092-5de1eaf8c46a',
        saved_amount=5000,
        status='On Track'
    )

    logging.info(response)


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