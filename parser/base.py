import json
from http import HTTPStatus
from typing import Optional

import aiohttp
from bs4 import BeautifulSoup


__all__ = ["BaseClient"]

class BaseClient:
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
    soup = BeautifulSoup(body, features="html.parser")
    result = soup.find("script", type="application/ld+json")
    amount_divs = soup.find_all("div", class_="discount_amount")
    result_json = json.loads(result.text)
    
    # Extract amount values (eg 2 l bottle or so)
    amounts = []
    for div in amount_divs:
        amount_text = div.text.strip().replace('\xa0', '')  # remove unicode special formatting
        start_index = amount_text.find('/') + 1
        end_index = amount_text.find('l') + 1 

        extracted_amount = amount_text[start_index:end_index].strip()
        amounts.append(extracted_amount)
        
    # Add drink amount to each offer 
    if 'offers' in result_json and 'offers' in result_json['offers']:
        offers = result_json['offers']['offers']

        for i, offer in enumerate(offers):
            offer['amount'] = amounts[i]

    return result_json


async def make_request(session, url, **kwargs):
    try:
        async with session.get(url, **kwargs) as response: 
            return check_result(url, response.status, await response.text())
    except aiohttp.ClientError as e:
        raise Exception(f"aiohttp client throws an error: {e}")
