import os
import jwt
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from backend.app.routes.auth import get_secret

bearer_scheme = HTTPBearer(auto_error=True)

def check_access_token(credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme)):
    """Function that checks if a user has a valid access token."""
    unauthorised = HTTPException(
    status_code=401,
    detail="Not authenticated",
    headers={"WWW-Authenticate": "Bearer"}
    )

    if credentials is None:
        raise unauthorised

    try:
        payload = jwt.decode(credentials.credentials, get_secret(), "HS256")
        user_id = int(payload["sub"])
        return user_id
    except:
        raise unauthorised
