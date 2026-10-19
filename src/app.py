from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.post("/")
def teste():
    return "2-1:"


app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_methods=["*"],
            allow_credentials=True, 
            allow_headers=["*"]
)
