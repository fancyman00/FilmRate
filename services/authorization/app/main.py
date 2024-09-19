import asyncio
import sys

from fastapi import FastAPI
from app.api.endpoints.users import router as users_router
from app.api.endpoints.auth import router as auth_router
from app.database.session import init_db

app = FastAPI()
app.include_router(auth_router)
app.include_router(users_router)


if __name__ == "__main__":
    if "--generate" in sys.argv:
        asyncio.run(init_db())
