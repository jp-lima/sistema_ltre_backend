from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from auth.routes import auth_routes

app = FastAPI()

app.include_router(auth_routes)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_credentials=True,
    allow_headers=["*"],
)
