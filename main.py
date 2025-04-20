from fastapi import FastAPI
from api_router import fetch, create, update, delete
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(fetch.router)
app.include_router(create.router)
app.include_router(update.router)
app.include_router(delete.router)

handler = Mangum(app)