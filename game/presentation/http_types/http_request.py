# from starlette.datastructures import Headers


class HttpRequest:
    def __init__(
        self,
        query_params,
        headers,
        body,
        path_params=None,
        url=None,
        ipv4=None,
    ) -> None:
        self.headers: dict = headers
        self.body = body
        self.query_params = query_params
        self.path_params = path_params
        self.url = url
        self.ipv4 = ipv4
