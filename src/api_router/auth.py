from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from authlib.integrations.starlette_client import OAuth
from pydantic import BaseModel
from typing import Optional
import httpx
import os

from logger import logging
from src.database_ops.fetch_db import FetchFirebase
from src.database_ops.services import Services


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


# ------------------------- Models -------------------------

class LoginRequest(BaseModel):
    email: Optional[str] = None
    phone: Optional[str] = None
    password: str

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

        response = JSONResponse({"message": "Login successful"})
        response.set_cookie(key="access_token", value=token, httponly=True)  # fixed line
        return response

    except Exception as e:
        logging.error(f"Error occurred while logging in: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error {e}")

# ------------------------- Google SSO routes ------------------------------

@router.get('/login/google')
async def login_google(request: Request):
    redirect_uri = request.url_for('auth_google_callback')  # Make sure function name matches
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