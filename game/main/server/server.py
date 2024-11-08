from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from game.main.routes.routes import (
    user_router,
    multiplication_game_router,
    authentication_router,
    classes_router,
)

app = FastAPI()

origins = [
    "http://localhost:8080/",  # Substitua pela origem do seu front-end
    "http://localhost:8080",
    "http://172.17.199.189:8080/",
    "http://172.17.199.189:8080",
    # Adicione outras origens se necessário
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(multiplication_game_router)
app.include_router(authentication_router)
app.include_router(classes_router)
