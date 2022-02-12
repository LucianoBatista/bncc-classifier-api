from fastapi import APIRouter

ml_model_router = APIRouter(prefix="/model")

from . import views
