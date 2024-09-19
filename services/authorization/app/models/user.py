from typing import Annotated

from sqlalchemy.orm import mapped_column, Mapped

from app.database.model import Base

intpk = Annotated[int, mapped_column(primary_key=True, index=True)]

class Users(Base):
    __tablename__ = "users"
    id: Mapped[intpk]
    email: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
