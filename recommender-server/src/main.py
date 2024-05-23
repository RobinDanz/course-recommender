from fastapi import FastAPI
from routers import users, auth, courses, forms
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from database.config import fill_db, str_to_time
from models.course import Course

@asynccontextmanager
async def lifespan(app: FastAPI):
    await fill_db()
    yield

app = FastAPI(lifespan=lifespan)


allowed_origins = [
    'http://localhost:5173'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(courses.router)
app.include_router(forms.router)

