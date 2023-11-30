from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from game.main.adapters.request_adapter import request_adapter
from game.main.composers.users_composers import (
    create_user_composer,
    handle_user_composer,
)
from game.presentation.http_types.http_response import HttpResponse

user_router = APIRouter()
# multiplication_game_router = APIRouter(prefix='multiplication_game_router')
# authentication_router = APIRouter(prefix='authentication_router')


@user_router.post("/user")
async def create_user(request: Request):
    print("Entrou")
    http_response = await request_adapter(request, create_user_composer())
    return http_response


@user_router.get("/user")
def handle_user(request: Request):
    http_response = request_adapter(request, handle_user_composer())
    return JSONResponse(http_response)
