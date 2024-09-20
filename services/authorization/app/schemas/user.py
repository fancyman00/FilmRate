from pydantic import BaseModel, EmailStr, SecretStr, Field, ConfigDict

config = ConfigDict(from_attributes=True)


class UserSchema(BaseModel):
    email: EmailStr = Field(
        title="User’s email", description="User’s email", examples=["alex@fancy.com"]
    )
    password: SecretStr = Field(
        title="User’s password",
        description="User’s password",
        examples=["@SuperSecret123"],
    )


class UserLogin(BaseModel):
    model_config = config
    email: EmailStr = Field(
        title="User’s email", description="User’s email", examples=["john@domain.com"]
    )
    password: SecretStr = Field(
        title="User’s password",
        description="User’s password",
        examples=["@SuperSecret123"],
    )
