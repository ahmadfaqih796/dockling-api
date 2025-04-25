from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.modules.user import user_router
from app.modules.gen.markdown import markdown_router

app = FastAPI()


app.title = "Docling API"
app.summary = "Created By Team"
app.description = "Ini adalah Docling App untuk generate markdown dari dokumen pdf"
app.version = "1.0.0"
# app.terms_of_service = "http://localhost/"
app.contact = {
    "name": "Team Hore",
    "url": "https://ahmadfaqih796.github.io/",
    "email": "ahmadfaqih796@gmail.com",
}
# app.include_router(user_router.router)
app.include_router(markdown_router.router)

app.mount("/static", StaticFiles(directory="uploads"), name="static")
# print("Nama Project:", settings.PROJECT_NAME)
# print("Versi:", settings.PROJECT_VERSION)
# print("Database URL:", settings.DATABASE_URL)