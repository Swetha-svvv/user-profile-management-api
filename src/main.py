from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.core.database import Base, SessionLocal, engine
from src.core.seed import seed_users

from src.api.routes.user_routes import router as user_router
from src.middleware.error_handler import register_exception_handlers


@asynccontextmanager
async def lifespan(app: FastAPI):

    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        seed_users(db)

    finally:
        db.close()

    yield


app = FastAPI(
    title="User Profile Management API",
    version="1.0.0",
    description="Resilient User Profile Management API with Data Enrichment",
    lifespan=lifespan
)

app.include_router(user_router)

@app.get("/")
def root():
    return {
        "message": "User Profile Management API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


register_exception_handlers(app)