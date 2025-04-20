import requests
from requests_auth_aws_sigv4 import AWSSigV4
import boto3

# base_url = 'http://192.168.1.103:8000'
base_url = 'https://ocywxhljowqwhsq7etp67qtepm0llgze.lambda-url.ap-south-1.on.aws'
auth = AWSSigV4(
    region='ap-south-1',
    service='lambda',
    credentials=boto3.Session().get_credentials()
)

# Payload
headers = {'Content-Type': 'application/json'}
data = {'user_id': 'af02a499-01b6-11f0-9306-00155d016700'}

response = requests.post(f'{base_url}/fetch/budgets/', headers=headers, json=data)
print(response.status_code)
print(type(response.json()['data']))
print(response.json())

# expense_id = '48ac5368-024f-11f0-87df-00155d92ba78'
# budget_id = '4924b9e6-024f-11f0-8eff-00155d92ba78'
# income_id = '4982166f-024f-11f0-8844-00155d92ba78'
# goal_id = '49dd3c7c-024f-11f0-8c02-00155d92ba78'
# payment_id = '4a3aebc9-024f-11f0-a9ee-00155d92ba78'
# notification_id = '4a9763a8-024f-11f0-a37b-00155d92ba78'


# ### 1️⃣ Delete Expense
# response = requests.delete(
#     f'{base_url}/delete/expense',
#     json={"user_id": user_id, "expense_id": expense_id},
#     headers=headers
# )
# print("Delete Expense:", response.json())

# ### 2️⃣ Delete Budget
# response = requests.delete(
#     f'{base_url}/delete/budget',
#     json={"user_id": user_id, "budget_id": budget_id},
#     headers=headers
# )
# print("Delete Budget:", response.json())

# ### 3️⃣ Delete Income
# response = requests.delete(
#     f'{base_url}/delete/income',
#     json={"user_id": user_id, "income_id": income_id},
#     headers=headers
# )
# print("Delete Income:", response.json())

# ### 4️⃣ Delete Goal
# response = requests.delete(
#     f'{base_url}/delete/goal',
#     json={"user_id": user_id, "goal_id": goal_id},
#     headers=headers
# )
# print("Delete Goal:", response.json())

# ### 5️⃣ Delete Recurring Payment
# response = requests.delete(
#     f'{base_url}/delete/recurring-payment',
#     json={"user_id": user_id, "payment_id": payment_id},
#     headers=headers
# )
# print("Delete Recurring Payment:", response.json())

# ### 6️⃣ Delete Notification
# response = requests.delete(
#     f'{base_url}/delete/notification',
#     json={"user_id": user_id, "notification_id": notification_id},
#     headers=headers
# )
# print("Delete Notification:", response.json())

# ### 7️⃣ Delete User (last step)
# response = requests.delete(
#     f'{base_url}/delete/user',
#     json={"user_id": user_id},
#     headers=headers
# )
# print("Delete User:", response.json())
