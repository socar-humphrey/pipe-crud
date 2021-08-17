from pydantic import BaseModel

class UserRegisterSchema(BaseModel):
    username: str
    password: str

class UserRegisterOutSchema(BaseModel): 
    id: str
    name: str

    class Config: 
        orm_mode = True