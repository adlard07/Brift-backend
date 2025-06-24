import os
from dataclasses import dataclass, field
from firebase_admin import db
from dotenv import load_dotenv

from logger import logging
from src.database_ops.firebase_auth import FirebaseAuth
from src.database_ops.services import Services

# Load environment variables
load_dotenv()

@dataclass
class FetchFirebase:
    auth_client: FirebaseAuth = field(default_factory=FirebaseAuth)
    db_services: Services = field(default_factory=Services)
    ref: db.Reference = field(init=False)

    def __post_init__(self):
        self.ref = self.auth_client.initialize_firebase_app()

    def fetch_user(self, user_id: str) -> dict:
        return self._fetch_path(user_id)

    def fetch_data(self, user_id: str, node: str) -> dict:
        return self._fetch_path(f"{user_id}/{node}")

    def _fetch_path(self, path: str) -> dict:
        try:
            data = self.ref.child(path).get()
            if not data:
                return {"status_code": 404, "error": f"No data found at path '{path}'"}
            return {"status_code": 200, "data": data}
        except Exception as e:
            logging.error(f"Error fetching data at path '{path}': {e}")
            return {"status_code": 500, "error": str(e)}



if __name__ == "__main__":
    fetch_db_object = FetchFirebase()
    user_id = 'd4df0759-3f8b-4a21-91a8-bd56229937df'

    data = fetch_db_object.fetch_data(user_id, 'budgets')
    print(data)