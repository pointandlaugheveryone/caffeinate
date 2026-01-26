from typing import Union
from .base import BaseClient
from .types import Discount


class KupiParser(BaseClient):
    async def get_prices(
        self,
        item_id: str
    ) -> Discount:

        page_url = 'https://www.kupi.cz/sleva/' + item_id
        results = await self.request(page_url)
        discount = Discount(**results)
            
        return discount