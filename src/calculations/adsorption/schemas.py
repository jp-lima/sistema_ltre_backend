from pydantic import BaseModel 

class FirstOrderLinarModelRequest(BaseModel):
    t: list[int]
    a: list[float] 
    b: float  






