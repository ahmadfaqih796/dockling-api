# from app.core.config import settings
from fastapi import FastAPI
from app.routers import user_router

app = FastAPI()

app.include_router(user_router.router)

# print("Nama Project:", settings.PROJECT_NAME)
# print("Versi:", settings.PROJECT_VERSION)
# print("Database URL:", settings.DATABASE_URL)