from fastapi import APIRouter

ml_model_router = APIRouter(prefix="/models")


@ml_model_router.get("/status")
def get_current_model():
    return {"AdaBufaClassifer": {"accuracy": 99.99, "recall": 99.99}}
