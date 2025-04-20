import firebase_admin
from firebase_admin import credentials
import time
import logging
from dotenv import load_dotenv

load_dotenv()

class FirebaseAuth:
    def __init__(self, creds_path="creds.json"):
        self.cred = credentials.Certificate(creds_path)
        if not firebase_admin._apps:
            firebase_admin.initialize_app(self.cred)
        self.token = None
        self.expiry_time = 0

    def get_firebase_access_token(self):
        """Return a cached token or refresh if expired."""
        try:
            # Refresh token if not available or expired
            if not self.token or time.time() >= self.expiry_time:
                access_token_info = self.cred.get_access_token()
                self.token = access_token_info.access_token
                self.expiry_time = time.time() + 3500  # 3500s ~ 58 min buffer
                logging.info("Refreshed Firebase token.")
            return self.token
        except Exception as e:
            logging.error(f"Error authenticating Firebase service account: {e}")
            return None

    def create_access_token(self, )


if __name__ == "__main__":
    auth_client = FirebaseAuth()
    token = auth_client.get_access_token()
    logging.info("Access Token:", token)
