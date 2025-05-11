import os
import firebase_admin
from firebase_admin import credentials, db
from dotenv import load_dotenv
from dataclasses import dataclass
from logger import logging

load_dotenv()

@dataclass
class FirebaseAuth:
    ref_path: str = "users"

    def initialize_firebase_app(self):
        try:
            if not firebase_admin._apps:
                cred = credentials.Certificate("creds.json")
                firebase_admin.initialize_app(cred, {
                    "databaseURL": os.getenv("FIREBASE_URL", "").rstrip("/")
                })
                logging.info("<-----Firebase initialized----->")

            return db.reference(self.ref_path)

        except Exception as e:
            logging.error(f"Could not initialize Firebase app: {e}")
            return None
