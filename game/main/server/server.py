from fastapi import FastAPI
from game.main.routes.routes import (
    user_router,
    multiplication_game_router,
    authentication_router,
)

app = FastAPI()
app.include_router(user_router)
app.include_router(multiplication_game_router)
app.include_router(authentication_router)
