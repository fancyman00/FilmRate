import time
import jwt

from app.config import settings as global_settings
from app.models.user import User

from fastapi import Request


def create_access_token(user: User, request: Request):
    payload = {
        "email": user.email,
        "expiry": time.time() + global_settings.JWT_ACCESS_TOKEN_EXPIRE,
        "platform": request.headers.get("User-Agent"),
    }
    token = jwt.encode(
        payload, str(user.password), algorithm=global_settings.JWT_ALGORITHM
    )

    return token


def create_refresh_token(user: User, request: Request):
    payload = {
        "email": user.email,
        "expiry": time.time() + global_settings.JWT_REFRESH_TOKEN_EXPIRE,
        "platform": request.headers.get("User-Agent"),
    }
    token = jwt.encode(
        payload, str(user.password), algorithm=global_settings.JWT_ALGORITHM
    )

    return token
