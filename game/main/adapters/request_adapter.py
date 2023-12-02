from typing import Callable
from game.presentation.http_types.http_request import HttpRequest
from game.presentation.http_types.http_response import HttpResponse
from fastapi import Request


async def request_adapter(request: Request, controller: Callable) -> HttpResponse:
    body = {}
    if request.body:
        body = request.body
    http_request = HttpRequest(
        body=body,
        headers=request.headers,
        query_params=request.query_params,
        path_params=request.path_params,
        url=request.url,
    )
    http_reponse = controller(http_request)
    return http_reponse
