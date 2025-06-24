from dataclasses import dataclass, field
from datetime import datetime, timedelta

from logger import logging
from src.database_ops.fetch import FetchFirebase
from src.models.QnA import QnA

@dataclass(kw_only=True)
class Dashboard:
    user_id: str
    fetch_db_object: FetchFirebase = field(default_factory=FetchFirebase)
    qna: QnA = field(default_factory=QnA)

    def total_spending(self):
        todays_spending = 0
        this_week_spending = 0
        this_month_spending = 0
        this_quarter_spending = 0
        past_6_months_spending = 0
        this_year_spending = 0
        all_time_spending = 0

        try:
            expenses = dict(self.fetch_db_object.fetch_data(self.user_id, 'expenses'))
            sorted_expenses = dict(sorted(expenses['data'].items(), key=lambda item: item[1]['date']))


            today = datetime.now().date()
            this_week_start_date = today - timedelta(days=today.weekday())
            this_week_dates = [this_week_start_date + timedelta(days=i) for i in range(7)]

            current_month = today.month
            current_year = today.year
            current_quarter = (today.month - 1) // 3 + 1
            six_months_ago = today - timedelta(days=182)

            for key, value in sorted_expenses.items():
                current_date = datetime.strptime(value['date'].split()[0], "%Y-%m-%d").date()
                amount = value['amount']

                # All-time
                all_time_spending += amount

                # Today's spending
                if current_date == today:
                    todays_spending += amount

                # This week's spending
                if current_date in this_week_dates:
                    this_week_spending += amount

                # This month's spending
                if current_date.month == current_month and current_date.year == current_year:
                    this_month_spending += amount

                # This quarter's spending
                quarter = (current_date.month - 1) // 3 + 1
                if current_date.year == current_year and quarter == current_quarter:
                    this_quarter_spending += amount

                # Past 6 months' spending
                if six_months_ago <= current_date <= today:
                    past_6_months_spending += amount

                # This year's spending
                if current_date.year == current_year:
                    this_year_spending += amount

        except Exception as e:
            logging.info(f"Error occured: {e}")

        finally:
            return {
                "todays_spending": todays_spending,
                "this_week_spending": this_week_spending,
                "this_month_spending": this_month_spending,
                "this_quarter_spending": this_quarter_spending,
                "past_6_months_spending": past_6_months_spending,
                "this_year_spending": this_year_spending,
                "all_time_spending": all_time_spending
                }

    def get_budgets(self):
        try:
            budgets = dict(self.fetch_db_object.fetch_data(self.user_id, 'budgets'))
            logging.info(f"{len(budgets)} budgets found.")
            return budgets['data']
        except Exception as e:
            logging.error(f"Error occured: {e}")

    def get_transactions(self):
        try:
            transactions = dict(self.fetch_db_object.fetch_data(self.user_id, 'expenses'))
            logging.info(f"{len(transactions)} transactions found.")
            return transactions['data']
        except Exception as e:
            logging.error(f"Error occured: {e}")


    # def get_savings(self):
    #     try:
    #         savings = dict(self.fetch_db_object.fetch_data(self.user_id, 'savings'))
    #     except Exception as e:
    #         logging.info(f"Error occured: {e}")
    #     finally:
    #         return 


if __name__=="__main__":
    user_id = "d4df0759-3f8b-4a21-91a8-bd56229937df"
    dashboard_object = Dashboard(user_id=user_id)
    result = dashboard_object.get_budgets()
    logging.info(result)