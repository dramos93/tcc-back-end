from typing import Dict


class HttpRequest:
    def __init__(
        self,
        query_params,
        headers=None,
        body: dict = {},
        path_params=None,
        url=None,
        ipv4=None,
    ) -> None:
        self.headers = headers
        self.body = body
        self.query_params = query_params
        self.path_params = path_params
        self.url = url
        self.ipv4 = ipv4
