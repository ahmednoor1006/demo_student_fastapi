from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from authlib.integrations.starlette_client import OAuth
from starlette.config import Config
import os
import crud, database, schemas, auth_utils
from auth_utils import create_access_token
from datetime import timedelta

router = APIRouter()

# OAuth configuration
config = Config()
oauth = OAuth(config)

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")

if GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET:
    oauth.register(
        name="google",
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
        client_kwargs={
            "scope": "openid email profile"
        }
    )

@router.get("/auth/login")
async def login(request: Request):
    """Initiate Google OAuth login"""
    if not GOOGLE_CLIENT_ID or not GOOGLE_CLIENT_SECRET:
        # fallback demo user
        access_token = create_access_token(
            data={"sub": "demo@example.com"},
            expires_delta=timedelta(minutes=60)
        )
        return RedirectResponse(
            url=f"/dashboard?token={access_token}&user_id=1&user_name=Demo User",
            status_code=302
        )
    
    redirect_uri = request.url_for("auth_callback")  # dynamic instead of hardcoded
    return await oauth.google.authorize_redirect(request, redirect_uri)

@router.get("/auth/callback", name="auth_callback")
async def auth_callback(request: Request, db: Session = Depends(database.get_db)):
    """Handle Google OAuth callback"""
    try:
        token = await oauth.google.authorize_access_token(request)
        user_info = token.get("userinfo")

        if not user_info:
            raise HTTPException(status_code=400, detail="Failed to get user info from Google")

        email = user_info.get("email")
        name = user_info.get("name")

        if not email:
            raise HTTPException(status_code=400, detail="Email not provided by Google")

        # Check if user exists
        user = crud.get_user_by_email(db, email)
        if not user:
            user_create = schemas.UserCreate(email=email, name=name)
            user = crud.create_user(db, user_create)

        # Create access token
        access_token = create_access_token(
            data={"sub": user.email},
            expires_delta=timedelta(minutes=60)
        )

        return RedirectResponse(
            url=f"/dashboard?token={access_token}&user_id={user.id}&user_name={user.name}",
            status_code=302
        )

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Authentication failed: {str(e)}")

@router.get("/auth/me")
async def get_current_user_info(current_user: schemas.User = Depends(auth_utils.get_current_user)):
    """Get current user information"""
    return current_user

@router.post("/auth/logout")
async def logout():
    """Logout endpoint"""
    return {"message": "Logged out successfully"}
