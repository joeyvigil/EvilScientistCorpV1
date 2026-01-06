from pydantic import BaseModel

# This MODEL class helps us MODEL data that we'll use throughout the app

class UserModel(BaseModel):
    id: int
    username: str
    password: str
    email: str