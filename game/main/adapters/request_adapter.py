from typing import Callable
from game.presentation.http_types.http_request import HttpRequest
from game.presentation.http_types.http_response import HttpResponse
from fastapi import Request
import json

async def request_adapter(request: Request, controller: Callable) -> HttpResponse:
    body = {}
    if request.body:
        body_request = await request.body()
        body = json.loads(body_request) if body_request else body
    http_request = HttpRequest(
        body= body,
        headers=request.headers,
        query_params=request.query_params,
        path_params=request.path_params,
        url=request.url,
    )
    http_reponse = controller(http_request)
    return http_reponse
