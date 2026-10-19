from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from sqlalchemy.ext.asyncio import AsyncSession

from auth.models import User
from auth.schema import (
    SchemaLoginRequest,
    SchemaRegisterRequest,
    SchemaUserResponse,
)
from auth.security import (
    create_access_token,
    delete_auth_cookie,
    get_current_user,
    set_auth_cookie,
)
from auth.services import authenticate_user, register_user
from database import get_db

auth_routes = APIRouter(tags=["Auth"])


@auth_routes.post(
    "/auth/register",
    response_model=SchemaUserResponse,
    status_code=status.HTTP_201_CREATED,
)
async def register(
    data: SchemaRegisterRequest,
    response: Response,
    db: AsyncSession = Depends(get_db),
):
    try:
        user = await register_user(db, data)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc

    token = create_access_token({"sub": str(user.id)})
    set_auth_cookie(response, token)
    return user


@auth_routes.post("/auth/login", response_model=SchemaUserResponse)
async def login(
    data: SchemaLoginRequest,
    response: Response,
    db: AsyncSession = Depends(get_db),
):
    user = await authenticate_user(db, data.email, data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    token = create_access_token({"sub": str(user.id)})
    set_auth_cookie(response, token)
    return user


@auth_routes.post("/auth/logout")
async def logout(response: Response):
    delete_auth_cookie(response)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@auth_routes.get("/auth/me", response_model=SchemaUserResponse)
async def me(
    request: Request,
    db: AsyncSession = Depends(get_db),
):
    user = await get_current_user(request, db, User)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )
    return user
