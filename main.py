from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

from src.api_router import auth, fetch, create, update, delete, dashboard

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(fetch.router)
app.include_router(create.router)
app.include_router(update.router)
app.include_router(delete.router)
app.include_router(dashboard.router)

handler = Mangum(app)