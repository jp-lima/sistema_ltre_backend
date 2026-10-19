from fastapi import APIRouter
from fastapi.responses import JSONResponse

auth_routes = APIRouter(tags=["Auth"])

@auth_routes.post("/auth/register")
async def register_user():
    pass 
