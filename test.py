import requests
from datetime import datetime
from src.database_ops.create import AddFirebase

base_url = 'http://127.0.0.1:9000'
# base_url = 'https://ocywxhljowqwhsq7etp67qtepm0llgze.lambda-url.ap-south-1.on.aws'

user_id = 'd4df0759-3f8b-4a21-91a8-bd56229937df'

# Create User Payload
headers = {'Content-Type': 'application/json'}

user_data = {
    "name": "Albina",
    "email": "albinadcunha@gmail.com",
    "password": "Adelard@123",
    "phone": "9323007428",
    # "device_id": "12394012964",
    # "created_at": str(datetime.now()),
    # "points": 10,
    # "store_unlocked": False,
    # "mfa_enabled": False,
    # "last_login": str(datetime.now()),
    # "currency": "INR",
    # "region": "India",
    # "backup_enabled": False,
}

response = requests.post(f'{base_url}/create/users', headers=headers, json=user_data)
print(response.status_code)
print(response.json())


# # expense_data = {
# #     "user_id": user_id,
# #     "amount": 200,
# #     "category": "Food",
# #     "notes": "Ordered ice-cream",
# #     "payment_method": "UPI",
# #     }

# # response = requests.post(f"{base_url}/create/expenses", headers=headers, json=expense_data)
# # print(response.status_code)
# # print(response.json())


# budget_data = {
#     "user_id": user_id,
#     "category": "Travel",
#     "note": "All travel related expenses are to be added here",
#     "amount_limit": 3000,
#     "interval": "monthly",
# }

# response = requests.post(f"{base_url}/create/budgets", headers=headers, json=budget_data)
# print(response.status_code)
# print(response.json())


# # income_data = {
# #     "user_id": user_id,
# #     "source": "Job",
# #     "title": "System Engineer at Eduvance",
# #     "amount": 33000,
# #     "date_received": "2025-04-06",
# # }

# # response = requests.post(f"{base_url}/create/incomes", headers=headers, json=income_data)
# # print(response.status_code)
# # print(response.json())


# # goal_data = {
# #     "user_id": user_id,
# #     "title": "Spend less than 3k on food this month",
# #     "target_amount": 2500,
# #     "due_date": "2025-05-26",
# # }

# # response = requests.post(f"{base_url}/create/goals", headers=headers, json=goal_data)
# # print(response.status_code)
# # print(response.json())



# # bill_data = {
# #     "user_id": user_id,
# #     "title": "Spotify",
# #     "amount": 199,
# #     "due_date": "2025-05-15",
# #     "is_paid": False,
# #     "recurring": True,
# # }

# # response = requests.post(f"{base_url}/create/bills", headers=headers, json=bill_data)
# # print(response.status_code)
# # print(response.json())



# # reminder_data = {
# #     "user_id": user_id,
# #     "title": "Pay Credit Card Bill",
# #     "description": "Don't forget to pay the credit card bill before due date.",
# #     "remind_at": str(datetime.now()),
# #     "linked_to": "bill_12345"
# # }

# # response = requests.post(f"{base_url}/create/reminders", headers=headers, json=reminder_data)
# # print(response.status_code)
# # print(response.json())



# # notification_data = {
# #     "user_id": user_id,
# #     "notification_type": "Reminder",
# #     "message": "Your electricity bill is due tomorrow.",
# #     "is_read": False,
# #     "is_valid": True
# # }

# # response = requests.post(f"{base_url}/create/notifications", headers=headers, json=notification_data)
# # print(response.status_code)
# # print(response.json())



# # debt_data = {
# #     "user_id": user_id,
# #     "title": "Personal Loan",
# #     "total_amount": 50000,
# #     "remaining_amount": 20000,
# #     "interest_rate": 10.5,
# #     "due_date": "2026-05-15",
# # }

# # response = requests.post(f"{base_url}/create/debts", headers=headers, json=debt_data)
# # print(response.status_code)
# # print(response.json())



# # investment_data = {
# #     "user_id": user_id,
# #     "title": "Mutual Fund",
# #     "amount_invested": 10000,
# #     "current_value": 11200,
# #     "date_invested": str(datetime.now()),
# #     "notes": "SIP investment in equity fund"
# # }

# # response = requests.post(f"{base_url}/create/investments", headers=headers, json=investment_data)
# # print(response.status_code)
# # print(response.json())

# # login_data = {
# #     "email": "adelarddcunha@gmail.com",
# #     "password": "Adelard@123"
# # }

# # response = requests.post(f"{base_url}/auth/login", headers=headers, json=login_data)
# # print(response.status_code)
# # print(response.json())



# user_query = "Give me all the expenses in the month of April."
# user_id = "d4df0759-3f8b-4a21-91a8-bd56229937df"

# qna_data = {
#     "user_query": user_query,
#     "user_id": user_id
# }

# response = requests.post(f"{base_url}/dashboard/qna", headers=headers, json=qna_data)
# print(response.status_code)
# print(response.json())


# transactions_data = {
# "user_id": "d4df0759-3f8b-4a21-91a8-bd56229937df"
# }
# response = requests.post(f"{base_url}/dashboard/transactions", headers=headers, json=transactions_data)
# print(response.status_code)
# print(response.json())

# create: AddFirebase = AddFirebase()
# user = create.create_user(new_user)