from fastapi.responses import JSONResponse
from dataclasses import dataclass, field
from dotenv import load_dotenv
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from datetime import datetime, timedelta
from firebase_admin import db
from passlib.hash import bcrypt
from jose import jwt
import os
import base64

from logger import logging
from src.database_ops.firebase_auth import FirebaseAuth

load_dotenv()

@dataclass
class Services:
    auth_client: FirebaseAuth = field(default_factory=FirebaseAuth)
    encryption_secret: str = str(os.getenv('ENCRYPTION_SECRET_KEY'))
    token_expiry: int = int(os.getenv('ASSESS_TOKEN_EXPIRY_HOURS'))
    token_secret: str = str(os.getenv('TOKEN_SECRET'))
    algorithm: str = "HS256"

    def __post_init__(self):
        self.ref: db.Reference = self.auth_client.initialize_firebase_app()
        self.key = self._generate_key()

# ----------------------- DB Services ---------------------------

    def fetch_user_by_field(self, field_name: str, value: str) -> dict:
        try:
            users = self.ref.order_by_child(field_name).equal_to(value).get()
            if users:
                return {"status_code": 200, "data": users}
            return {"status_code": 404, "error": "User not found"}
        except Exception as e:
            logging.error(f"Error fetching user by {field_name}: {e}")
            return {"status_code": 500, "error": f"Could not fetch user: {str(e)}"}

# ----------------------- Encryption/Decryption------------------------------

    def _generate_key(self) -> bytes:
        if not self.encryption_secret:
            raise ValueError("SECRET_KEY not found in environment variables.")
        return self.encryption_secret.encode('utf-8')[:32].ljust(32, b'0')

    def encrypt_text(self, plaintext: str) -> str:
        try:
            iv = os.urandom(16)
            padder = padding.PKCS7(128).padder()
            padded_data = padder.update(plaintext.encode('utf-8')) + padder.finalize()

            cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
            encryptor = cipher.encryptor()
            ciphertext = encryptor.update(padded_data) + encryptor.finalize()

            return base64.b64encode(iv + ciphertext).decode('utf-8')
        except Exception as e:
            logging.error(f"Error encrypting text: {e}")
            return None

    def decrypt_text(self, encrypted_text: str) -> str:
        try:
            raw_data = base64.b64decode(encrypted_text)
            iv = raw_data[:16]
            ciphertext = raw_data[16:]

            cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

            unpadder = padding.PKCS7(128).unpadder()
            plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

            return plaintext.decode('utf-8')
        except Exception as e:
            logging.error(f"Error decrypting text: {e}")
            return None

# ------------------------------ Token ---------------------------------


    def create_token(self, email: str):
        exp = datetime.utcnow() + timedelta(hours=self.token_expiry)
        return jwt.encode({"sub": email, "exp": exp}, self.token_secret, algorithm=self.algorithm)


if __name__ == "__main__":
    db_services = Services()
    user = db_services.fetch_user_by_field('profile/email', 'adelarddcunha@gmail.com')
    print("User id:", list(user['data'])[0])

    text = "this is my plain text"
    encrypted = db_services.encrypt_text(text)
    print("Encrypted:", encrypted)

    decrypted = db_services.decrypt_text(encrypted)
    print("Decrypted:", decrypted)
