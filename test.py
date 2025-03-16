import firebase_admin
from firebase_admin import credentials, auth

# Load your Firebase Service Account JSON file
cred = credentials.Certificate("credentials.json")

# Initialize Firebase Admin SDK
firebase_admin.initialize_app(cred)

def generate_custom_token(uid):
    """Generates a custom token for the given user ID."""
    try:
        custom_token = auth.create_custom_token(uid)
        return custom_token.decode("utf-8")
    except Exception as e:
        print(f"Error generating custom token: {e}")
        return None

# Example usage
uid = "user_12345"  # This should be the user's unique ID
token = generate_custom_token(uid)
print("Generated Token:", token)
