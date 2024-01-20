from fastapi import APIRouter, HTTPException, Request, status, Response
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
from game.main.composers.classes_composer import get_class_composer

user_router = APIRouter()
multiplication_game_router = APIRouter()
authentication_router = APIRouter()
classes_router = APIRouter()

# from fastapi.security import APIKeyHeader
# api_key_header = APIKeyHeader(name="x-api-key")


@user_router.post("/user")
async def create_user(request: Request) -> Response:
    try:
        http_response = await request_adapter(request, create_user_composer())
        breakpoint()
        return http_response
    except Exception as e:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e, headers={"message": "vaimbora"})


@user_router.get("/user")
async def handle_user(request: Request):
    try:
        http_response = await request_adapter(request, handle_user_composer())
        return http_response
    except Exception as e:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)


@multiplication_game_router.post("/multiplication-game")
async def create_game(request: Request):
    try:
        http_reponse = await request_adapter(
            request, create_multiplication_game_composer()
        )
        return http_reponse
    except Exception as e:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)


@multiplication_game_router.get("/multiplication-game")
async def get_all(request: Request):
    try:
        http_reponse = await request_adapter(
            request, get_all_multiplication_game_composer()
        )
        return http_reponse
    except Exception as e:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)


@authentication_router.post("/auth")
async def create_token(request: Request):
    try:
        http_response = await request_adapter(request, create_token_composer())
        return http_response
    except Exception as e:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)


@authentication_router.get("/auth")
async def get_by_id(request: Request):
    try:
        http_response = await request_adapter(request, get_token_composer())
        return http_response
    except Exception as e:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)


@authentication_router.post("/logout")
async def logout(request: Request):
    try:
        http_response = await request_adapter(request, logout_composer())
        return http_response
    except Exception as e:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)


@classes_router.get("/get_class_from_teacher")
async def get_class_from_teacher(request: Request):
    try:
        http_response = await request_adapter(request, get_class_composer())
        return http_response
    except Exception as e:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)
