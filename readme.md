# 💸 SpendWise - Personal Finance Tracker

SpendWise is a cross-platform mobile app built with **Flutter** and **Firebase** to help users manage expenses, set financial goals, track income, handle budgets, and receive smart insights powered by AI.

---

## 📱 Features

### ✅ Core Functionalities

- 🔐 **User Authentication**
  - Email & Password login
  - Google/Apple Sign-In
  - Biometric Login (Face ID / Fingerprint)

- 💸 **Expense Tracking**
  - Log daily expenses with categories and receipts
  - Filter and analyze expense trends
  - Attach photos via OCR receipt scanner

- 💰 **Income Management**
  - Track recurring and one-time income sources
  - Compare income vs. expenses

- 📊 **Budgeting**
  - Set budgets by category (e.g., Food, Transport)
  - Visual progress tracking and alerts

- 🎯 **Savings Goals**
  - Create financial goals with deadlines
  - Track progress toward saving targets

- 🔁 **Recurring Payments**
  - Manage subscriptions, loan EMIs, and bills
  - Set up auto-pay reminders

- 🔔 **Smart Notifications**
  - Budget alerts
  - Bill reminders
  - Goal updates

- 📈 **Financial Insights**
  - AI-powered spending analysis
  - Visual reports and forecasts
  - Monthly summary reports

- 💬 **AI Assistant (Chatbot)**
  - Ask natural questions like:
    - “How much did I spend on food last month?”
    - “Which category exceeded my budget?”

---

## 🔧 Tech Stack

| Layer         | Technology          |
|---------------|---------------------|
| **Frontend**  | Flutter (Dart)      |
| **Backend**   | Firebase Firestore  |
| **Auth**      | Python              |
| **Backend**   | FastAPI             |
| **Storage**   | Firebase Storage    |
| **OCR**       | Google ML Kit / Tesseract OCR |
| **Notifications** | Firebase Cloud Messaging |
| **State Management** | Riverpod / Provider / BLoC |
| **Analytics** | Custom logic + `fl_chart` |

---

## 🧱 Firebase Schema Overview

- `/users/{user_id}`  
  Stores user profile, with subcollections:
  - `expenses`
  - `income`
  - `budgets`
  - `goals`
  - `recurring_payments`
  - `notifications`

- Each subcollection contains documents with fields representing:
  - Amounts, categories, timestamps, statuses, etc.
  - Relationships across expenses, budgets, and goals.

---

## 🚀 Getting Started

### 🛠 Prerequisites

- Flutter SDK (>= 3.x)
- Dart SDK
- Firebase CLI
- Android Studio / Xcode
- Firebase project setup

### 🔥 Firebase Setup

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Create a new project
3. Add Firebase to Android/iOS apps
4. Download and place:
   - `google-services.json` in `android/app/`
   - `GoogleService-Info.plist` in `ios/Runner/`

5. Enable:
   - **Authentication** (Email/Password, Google)
   - **Firestore Database**
   - **Firebase Storage**
   - **Cloud Messaging** (for notifications)

### 📦 Install Dependencies

```bash
flutter pub get
