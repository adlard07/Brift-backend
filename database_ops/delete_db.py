import os
import requests
from dataclasses import dataclass, field
from dotenv import load_dotenv

from firebase_admin import credentials, db

from logger import logging
from database_ops.auth import FirebaseAuth
from database_ops.services import DBServices

@dataclass
class DeleteFirebase:
    auth_client: FirebaseAuth = field(default_factory=FirebaseAuth)
    db_services: DBServices = field(default_factory=DBServices)
    ref: db.Reference = field(init=False)

    def __post_init__(self):
        self.ref = self.auth_client.initialize_firebase_app('user')


    def delete_user(self, email: str) -> dict:
        return self.ref(f"{email}/")

    def delete_expense(self, email: str, expense_id: str) -> dict:
        return self.ref(f"{email}/expenses/{expense_id}")

    def delete_budget(self, email: str, budget_id: str) -> dict:
        return self.ref(f"{email}/budgets/{budget_id}")

    def delete_income(self, email: str, income_id: str) -> dict:
        return self.ref(f"{email}/income/{income_id}")

    def delete_goal(self, email: str, goal_id: str) -> dict:
        return self.ref(f"{email}/goals/{goal_id}")

    def delete_notification(self, email: str, notification_id: str) -> dict:
        return self.ref(f"{email}/notifications/{notification_id}")



if __name__=="__main__":

    firebase_deleter = DeleteFirebase()
    email = 'albinadcunha1970@gmail.com'

    # Delete a specific expense
    response = firebase_deleter.delete_expense(
        email=email, 
        expense_id="36684e39-01c1-11f0-a0ea-00155d016700")
    print(response)

    # Delete a budget
    response = firebase_deleter.delete_budget(
        email=email, 
        budget_id="36c04c2a-01c1-11f0-83ad-00155d016700")
    print(response)

    # Delete an income entry
    response = firebase_deleter.delete_income(
        email=email, 
        income_id="3717c35a-01c1-11f0-af25-00155d016700")
    print(response)

    # Delete a financial goal
    response = firebase_deleter.delete_goal(
        email=email, 
        goal_id="376e8764-01c1-11f0-82ba-00155d016700")
    print(response)

    # Delete a recurring payment
    response = firebase_deleter.delete_recurring_payment(
        email=email, 
        payment_id="37c744ae-01c1-11f0-ae46-00155d016700")
    print(response)

    # Delete a notification
    response = firebase_deleter.delete_notification(
        email=email, 
        notification_id="381d4395-01c1-11f0-8af4-00155d016700")
    print(response)

    # Delete a user
    response = firebase_deleter.delete_user(
        email=email)
    print(response)