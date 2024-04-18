from fastapi import FastAPI
from app.routes.router import router

app = FastAPI(title='SERVICE SOCIAL MEDIA V2')

app.include_router(router)
