from fastapi import APIRouter
from app.routes.tiktok import router as tiktok

router = APIRouter()

router.include_router(tiktok, tags=["Get Following & Followers"], prefix="/Tiktok")