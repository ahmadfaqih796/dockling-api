# from app.core.config import settings
from fastapi import FastAPI
from app.modules.user import user_router

app = FastAPI()


app.title = "Docling App"
app.summary = "Hallo ini sumeru"
app.version = "99.0.0"
app.terms_of_service = "http://localhost/"
app.contact = {
    "name": "Faqih Games",
    "url": "http://localhost/",
    "email": "t6gZi@example.com",
}
app.include_router(user_router.router)

# print("Nama Project:", settings.PROJECT_NAME)
# print("Versi:", settings.PROJECT_VERSION)
# print("Database URL:", settings.DATABASE_URL)