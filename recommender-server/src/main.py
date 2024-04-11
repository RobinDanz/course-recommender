from fastapi import FastAPI
from routers import users, auth, test
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

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
app.include_router(test.router)
