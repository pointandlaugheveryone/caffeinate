import json
import logging
from http import HTTPStatus
from typing import Optional

import aiohttp
from bs4 import BeautifulSoup

from . import exceptions


log = logging.getLogger("pykupi")

__all__ = ["BaseClient"]


class BaseClient:
    """
    The base class for implementing the main methods for requesting web pages.
    """
    def __init__(self):
        self._session: Optional[aiohttp.ClientSession] = None

    @property
    def session(self) -> Optional[aiohttp.ClientSession]:
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession(json_serialize=json.dumps)
        return self._session

    async def request(self, url) -> dict:
        return await make_request(self.session, url)


def check_result(url: str, status_code: int, body: str):
    log.debug("Response from server (%s): [%d]", url, status_code)
    soup = BeautifulSoup(body, features="html.parser")
    result = soup.find("script", type="application/ld+json")
    if result is None:
        raise exceptions.APIError("Can't parse page data'")
    result = result.text
    try:
        result_json = json.loads(result)
    except ValueError:
        result_json = {}
    if status_code == HTTPStatus.NOT_FOUND:
        raise exceptions.PageNotFound("Not found")
    elif HTTPStatus.OK <= status_code <= HTTPStatus.IM_USED:
        return result_json
    elif status_code >= HTTPStatus.BAD_REQUEST:
        raise exceptions.ServerError("Server error [{}]: ".format(status_code))


async def make_request(session, url, **kwargs):
    log.debug('Make GET request: "%s"', url)
    try:
        async with session.get(url, **kwargs) as response:
            return check_result(url, response.status, await response.text())
    except aiohttp.ClientError as e:
        raise Exception(f"aiohttp client throws an error: {e.__class__.__name__}: {e}")
