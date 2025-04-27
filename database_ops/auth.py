import os
import firebase_admin
from firebase_admin import credentials, db
from dotenv import load_dotenv
from dataclasses import dataclass, field

load_dotenv()

@dataclass
class FirebaseAuth:
    def initialize_firebase_app(self, ref):
        if not firebase_admin._apps:
            cred = credentials.Certificate("creds.json")
            firebase_admin.initialize_app(cred, {
                "databaseURL": os.getenv("FIREBASE_URL", "").rstrip("/")
            })
        return db.reference(ref)


    # def create_access_token(self, ):


if __name__ == "__main__":
    auth_client = FirebaseAuth()
    ref = auth_client.initialize_app()
    logging.info("Firebase app initialized.")
