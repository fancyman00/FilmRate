from pydantic import BaseModel, EmailStr, SecretStr, Field


class UserSchema(BaseModel):
    email: EmailStr = Field(
        title="User’s email", description="User’s email", examples=["alex@fancy.com"]
    )
    password: SecretStr = Field(
        title="User’s password",
        description="User’s password",
        examples=["@SuperSecret123"],
    )

