class ServerError(Exception):
    pass


class APIError(Exception):
    pass


class PageNotFound(APIError):
    pass
