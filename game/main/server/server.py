from fastapi import FastAPI
from game.main.routes.routes import user_router

app = FastAPI()
app.include_router(user_router)
