from fastapi import APIRouter, HTTPException, Response, Request, Query
from bson import ObjectId
import json
import io
import os
from dotenv import load_dotenv
from fastapi.responses import FileResponse, StreamingResponse
from ..service.tiktok import Tiktok

load_dotenv()

router = APIRouter()

@router.get("/following")
async def get_following(username: str, limit: int = 10):
    response = Tiktok().following(username=username, limit=limit)
    return response

@router.get("/followers")
async def get_followers(username: str, limit: int = 10):
    response = Tiktok().followers(username=username, limit=limit)
    return response