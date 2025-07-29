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
    amount_divs = soup.find_all("div", class_="discount_amount left")

    if result is None or amount_divs is None:
        raise exceptions.APIError("Can't parse page data")
    
    try:
        result_json = json.loads(result.text)
        
        # Extract amount values (eg 2 l bottle or so)
        amounts = []
        for div in amount_divs:
            amount_text = div.text.strip().replace('\xa0', '')  # remove unicode NBSP formatting
            start_index = amount_text.find('/') + 1
            end_index = amount_text.find('l') + 1  # want to keep the l there

            extracted_amount = amount_text[start_index:end_index].strip()
            amounts.append(extracted_amount)
         
        # Add amounts to offers in JSON
        if 'offers' in result_json and 'offers' in result_json['offers']:
            offers = result_json['offers']['offers']

            for i, offer in enumerate(offers):
                if i < len(amounts):
                    offer['amount'] = amounts[i]

        return result_json

    except ValueError as e:
        print("JSON parsing error:", e)
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
