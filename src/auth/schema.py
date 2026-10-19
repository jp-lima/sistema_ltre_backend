from pydantic import BaseModel

class SchemaAuthRequest(BaseModel):
    name:str
    email: str 
    password: str

