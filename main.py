from fastapi import FastAPI
from api_router import create, update, delete

app = FastAPI()

app.include_router(create.router)
app.include_router(update.router)
app.include_router(delete.router)