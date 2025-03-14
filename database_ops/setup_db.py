import os
import requests
import json
from dataclasses import dataclass
from dotenv import load_dotenv

from logger import logging

load_dotenv()

@dataclass
class CreateFirebaseDB:
    base_url = os.getenv('BASE_URL')
    table_names = [
    'users', 'expences', 'budgets', 'income', 
    'goals', 'recurring_payments', 'notifications',
    ]

    def __post_init__(self):
        try:
            requests.put(self.base_url)
        except Exception as e:
            logging.info(f'Error occured: {e}')


    def create_tables(self) -> None:
        try:

            # for table_name in self.table_names:
            #     requests.get(self.base_url + table_name + '.json')
            # logging.info("--Tables created--")
        
        except Exception as e:
            logging.info(f"Error occured at {e}")
        
        return None


if __name__=="__main__":
    firebase_object = CreateFirebaseDB()
    firebase_object.create_tables()