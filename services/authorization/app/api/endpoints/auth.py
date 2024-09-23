
from fastapi import APIRouter, Depends, Request, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.models.user import User
from app.schemas.user import UserSchema, UserLogin
from app.services.auth import create_access_token, create_refresh_token
from app.tasks.email import verify_email

router = APIRouter(prefix='/auth', tags=['Auth'])


@router.post('/signup/')
async def signup(payload: UserSchema, request: Request, db_session: AsyncSession = Depends(get_db)):
    _user: User = User(**payload.model_dump())
    if not await User.find(db_session, [User.email == _user.email]):
        await _user.save(db_session)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User is already exist"
        )
    verify_email.delay(_user.email)
    # _user.access_token = create_access_token(_user, request)
    # _user.refresh_token = create_refresh_token(_user, request)
    return _user


@router.post('/signin/')
async def signin(payload: UserLogin, request: Request, db_session: AsyncSession = Depends(get_db)):
    _user: User = await User.find(db_session, [User.email == payload.email])

    if not _user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    if not _user.check_password(payload.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Password is incorrect"
        )
    _user.access_token = create_access_token(_user, request)
    _user.refresh_token = create_refresh_token(_user, request)
    return _user
