from fastapi import APIRouter, Request
from game.main.adapters.request_adapter import request_adapter
from game.main.composers.users_composers import (
    create_user_composer,
    handle_user_composer,
)
from game.main.composers.authentication_composer import (
    create_token_composer,
    get_token_composer,
    logout_composer,
)
from game.main.composers.multiplication_game_composer import (
    create_multiplication_game_composer,
    get_all_multiplication_game_composer,
)

user_router = APIRouter()
multiplication_game_router = APIRouter()
authentication_router = APIRouter()


@user_router.post("/user")
async def create_user(request: Request):
    print("Entrou")
    http_response = await request_adapter(request, create_user_composer())
    return http_response


@user_router.get("/user")
async def handle_user(request: Request):
    http_response = await request_adapter(request, handle_user_composer())
    return http_response


@multiplication_game_router.post("/multiplication-game")
async def create_game(request: Request):
    http_reponse = await request_adapter(request, create_multiplication_game_composer())
    return http_reponse


@multiplication_game_router.get("/multiplication-game")
async def get_all(request: Request):
    http_reponse = await request_adapter(
        request, get_all_multiplication_game_composer()
    )
    return http_reponse


@authentication_router.post("/auth")
async def create_token(request: Request):
    http_response = await request_adapter(request, create_token_composer())
    return http_response


@authentication_router.get("/auth")
async def get_by_id(request: Request):
    http_response = await request_adapter(request, get_token_composer())
    return http_response


@authentication_router.post("/logout")
async def logout(request: Request):
    http_response = await request_adapter(request, logout_composer())
    return http_response
