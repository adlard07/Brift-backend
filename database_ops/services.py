from dataclasses import dataclass, field
from dotenv import load_dotenv
import os
import firebase_admin
from firebase_admin import credentials, db

from logger import logging
from database_ops.auth import FirebaseAuth

# Load environment variables
load_dotenv()

@dataclass
class DBServices:
    auth_client: FirebaseAuth = field(default_factory=FirebaseAuth)

    def fetch_user_by_field(self, field_name: str, value: str, ref: db.Reference):
        try:
            users = ref.order_by_child(field_name).equal_to(value).get()
            if users:
                return users
            return {}
        except Exception as e:
            logging.error(f"Error fetching user by {field_name}: {e}")
            return {"status_code": 500, "error": f"Could not fetch user: {e}"}


if __name__ == "__main__":
    from database_ops.auth import FirebaseAuth

    db_services = DBServices()
    firebase_object = FirebaseAuth()

    result = db_services.fetch_user_by_field("profile/email", "adelarddcunha07@gmail.com", firebase_object.initialize_firebase_app('user'))
    logging.info(result)
    logging.info(bool(result))
