from fastapi import FastAPI
from project.app.config import settings


def create_app() -> FastAPI:
    app = FastAPI()

    from project.app.api import ml_model

    app.include_router(ml_model.ml_model_router)

    @app.get("/")
    def root():
        return {"config": settings.DATABASE_URL}

    return app
