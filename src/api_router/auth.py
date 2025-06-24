from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from authlib.integrations.starlette_client import OAuth
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import httpx
import os

from logger import logging
from src.database_ops.fetch import FetchFirebase
from src.database_ops.services import Services
from src.database_ops.create import AddFirebase

router = APIRouter(
    prefix='/auth',
    tags=['auth']
    )

oauth = OAuth()
oauth.register(
    name='google',
    client_id=os.getenv('GOOGLE_CLIENT_ID'),
    client_secret=os.getenv('GOOGLE_CLIENT_SECRET'),
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid email profile'
    }
)

services: Services = Services()
create: AddFirebase = AddFirebase()

# ------------------------- Models -------------------------

class LoginRequest(BaseModel):
    email: str
    password: str

class SigninRequest(BaseModel):
    name: str
    email: str
    password: str
    phone: str
    device_id: Optional[str] = None
    points: Optional[int] = 10
    store_unlocked: Optional[bool] = False
    mfa_enabled: Optional[bool] = False
    currency: Optional[str] = "INR"
    region: Optional[str] = "IND"
    backup_enabled: Optional[bool] = False
    created_at: Optional[str] = str(datetime.now())
    last_login: Optional[str] = str(datetime.now())

# ------------------------- Routes -------------------------

@router.post('/login')
async def login(payload: LoginRequest):
    try:
        user_response = services.fetch_user_by_field('profile/email', str(payload.email))
        if user_response["status_code"] != 200:
            raise HTTPException(status_code=404, detail="User does not exist")
        
        users = user_response["data"]
        user_data = next(iter(users.values()))  # Get first (and ideally only) user
        profile = user_data.get('profile', {})

        encrypted_password = profile.get('password')
        if not encrypted_password:
            raise HTTPException(status_code=500, detail="Encrypted password not found")

        decrypted_password = services.decrypt_text(encrypted_password)

        if not decrypted_password or decrypted_password != payload.password:
            raise HTTPException(status_code=401, detail="Invalid credentials")

        token = services.create_token(email=profile.get('email'))
        user_id = list(users)[0]
        logging.info(f"User with user_id '{user_id}' logged in.")

        return {"message": "Login successful", "access_token": token, "user_id": user_id}
    except Exception as e:
        logging.error(f"Error occurred while logging in: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error {e}")


@router.post('/signin')
async def signin(payload: SigninRequest):
    try:
        # Check if user already exists
        existing_email = services.fetch_user_by_field('profile/email', str(payload.email))
        if existing_email["status_code"] == 200 and existing_email["data"]:
            raise HTTPException(status_code=409, detail="User already exists")
        existing_phone = services.fetch_user_by_field('profile/phone', str(payload.phone))
        if existing_phone["status_code"] == 200 and existing_phone["data"]:
            raise HTTPException(status_code=409, detail="User already exists")

        # Encrypt password
        encrypted_password = services.encrypt_text(payload.password)

        # Create user payload
        profile = {
            "name": payload.name,
            "email": payload.email,
            "password": encrypted_password,
            "phone": payload.phone,
            "created_at": payload.created_at,
            "device_id": payload.device_id,
            "points": payload.points,
            "store_unlocked": payload.store_unlocked,
            "mfa_enabled": payload.mfa_enabled,
            "last_login": payload.last_login,
        }   

        settings = {
            "backup_enabled": payload.backup_enabled,
            "currency": payload.currency,
            "region": payload.region,
        }

        user = create.create_user(profile, settings)
        logging.info(f"User created: {user}")

        if user["status_code"] not in (200, 201):
            raise HTTPException(status_code=500, detail="Failed to create user")

        # Create JWT token
        token = services.create_token(email=payload.email)

        return {"message": "User created successfully", "access_token": token, "user_id": user['user_id']}

    except Exception as e:
        logging.error(f"Error during sign in: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error {e}")


# ------------------------- Google SSO routes ------------------------------

@router.get('/login/google')
async def login_google(request: Request):
    redirect_uri = request.url_for('auth_google_callback')
    return await oauth.google.authorize_redirect(request, redirect_uri)


@router.get('/login/google/callback')
async def auth_google_callback(request: Request):
    token = await oauth.google.authorize_access_token(request)
    user_info = await oauth.google.parse_id_token(request, token)

    email = user_info.get('email')
    name = user_info.get('name')
    profile_picture = user_info.get('picture')

    return {
        "email": email,
        "name": name,
        "profile_picture": profile_picture
    }