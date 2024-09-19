from fastapi import APIRouter

from app.schemas.users import UserData

router = APIRouter(prefix='/auth', tags=['Auth'])


@router.post('/register/')
async def register_user(user_data: UserData):
    print(user_data)
    pass
