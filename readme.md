# SpendWise 
---
## Database Schema (Firebase Firestore)

### Collections and Relationships

#### 1. Users Collection
**Path:** `/users/{user_id}`  
Stores user information and acts as the root collection for all user-related data.

**Fields:**
- `user_id`: Unique identifier for the user.
- `username`: Display name of the user.
- `email`: Registered email address.
- `password_hash`: Hashed password for authentication.
- `created_at`: Timestamp of user registration.

**Relationships:**
- Each user has **subcollections** for expenses, budgets, income, goals, recurring payments, and notifications.

---

#### 2. Expenses Collection
**Path:** `/users/{user_id}/expenses/{expense_id}`  
Stores all expenses related to a specific user.

**Fields:**
- `expense_id`: Unique identifier for the expense.
- `category`: Type of expense (e.g., Food, Transport).
- `amount`: Expense amount.
- `date`: Timestamp when the expense occurred.
- `note`: Additional details about the expense.
- `payment_method`: Method used for payment.
- `receipt_url`: Reference to stored receipt (if applicable).

**Relationships:**
- Linked to `users` collection through `user_id` in the parent document path.
- Can be cross-referenced with `budgets` for spending tracking.

---

#### 3. Budgets Collection
**Path:** `/users/{user_id}/budgets/{budget_id}`  
Stores budget allocations and usage tracking.

**Fields:**
- `budget_id`: Unique identifier for the budget.
- `category`: Expense category associated with the budget.
- `amount`: Allocated budget amount.
- `period`: Duration (e.g., Weekly, Monthly).
- `used_amount`: Amount already spent.
- `created_at`: Timestamp of budget creation.

**Relationships:**
- Linked to `expenses` to track spending against budget.

---

#### 4. Income Collection
**Path:** `/users/{user_id}/income/{income_id}`  
Tracks income sources and earnings.

**Fields:**
- `income_id`: Unique identifier for the income entry.
- `source`: Source of income (e.g., Salary, Freelance).
- `amount`: Income amount.
- `frequency`: Recurrence pattern (e.g., Monthly, Weekly).
- `date_received`: Timestamp of income entry.

**Relationships:**
- Linked to `users` collection.

---

#### 5. Goals Collection
**Path:** `/users/{user_id}/goals/{goal_id}`  
Stores financial goals and progress tracking.

**Fields:**
- `goal_id`: Unique identifier for the goal.
- `title`: Description of the goal.
- `target_amount`: Desired savings amount.
- `saved_amount`: Current savings progress.
- `deadline`: Goal completion deadline.
- `status`: Status of the goal (e.g., In Progress, Completed).

**Relationships:**
- Linked to `income` collection to track funding sources.

---

#### 6. Recurring Payments Collection
**Path:** `/users/{user_id}/recurring_payments/{payment_id}`  
Manages recurring transactions such as subscriptions, loans, or utility bills.

**Fields:**
- `payment_id`: Unique identifier for the payment.
- `service_name`: Name of the service.
- `amount`: Payment amount.
- `payment_date`: Due date for the payment.
- `frequency`: Recurrence pattern (e.g., Monthly, Annually).
- `auto_deduct`: Boolean indicating if automatic payments are enabled.

**Relationships:**
- Linked to `expenses` collection to track recurring deductions.

---

#### 7. Notifications Collection
**Path:** `/users/{user_id}/notifications/{notification_id}`  
Stores system-generated notifications for budget alerts, due payments, or financial insights.

**Fields:**
- `notification_id`: Unique identifier for the notification.
- `message`: Notification content.
- `type`: Type of notification (e.g., Budget Alert, Payment Reminder).
- `timestamp`: When the notification was triggered.
- `read`: Boolean indicating if the notification has been viewed.

**Relationships:**
- Linked to `users` collection.
- Can reference `budgets` or `expenses` for triggered alerts.

---

### Issues occured and their resolution while development:
1. 	- Issue: the `firebase_admin` module in python wasn't able to read project credentials.
	- Resolved by: using `requests` module in python to request the firebase reatime database API and wrote custom functions using GET, POST, PUT and DELETE request type to communicate with firebase.
